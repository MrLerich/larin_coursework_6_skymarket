from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from ads.filters import AdFilter
from ads.models import Ad, Comment
from ads.permissions import IsOwner
from ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = AdPagination
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend,) # Подключаем библотеку, отвечающую за фильтрацию к CBV
    filterset_class = AdFilter# Выбираем наш фильтр

    def get_serializer_class(self):
        if self.action in ['retrieve']:
            return AdDetailSerializer
        else:
            return AdSerializer

    def get_permission(self):
        if self.action in ['update', 'destroy', 'partial_update', 'create', 'me']:
            self.permission_classes = [IsAuthenticated, IsAdminUser | IsOwner]
        # elif self.action['retrieve']:
        #     self.permission_classes = [AllowAny]
        return super().get_permissions()

    @action(detail=False)
    def me(self, request, *args, **kwargs):
        self.queryset = Ad.objects.filter(author=request.user)
        return super().list(self, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):  # переопределяем по номеру объявления коменты  к этому же объявлению
        ad_id = self.kwargs.get('ad_pk')
        return Comment.objects.filter(ad_id=ad_id)

    # def get_queryset(self):
    #     ad_id = self.kwargs.get("ad_pk")
    #     ad_instance = get_object_or_404(Ad, id=ad_id)
    #     return ad_instance.comments.all()

    def perform_create(self, serializer):
        ad_id = self.kwargs.get('ad_pk')
        ad_instance = get_object_or_404(Ad, pk=ad_id)
        user = self.request.user
        serializer.save(author=user, ad=ad_instance)
