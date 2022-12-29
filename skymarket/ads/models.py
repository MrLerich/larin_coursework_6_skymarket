from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=250,
                             help_text="Введите название товара",
                             unique=True)
    price = models.PositiveIntegerField(verbose_name="Цена товара",
                                        help_text="Укажите цену товара")
    description = models.TextField(blank=True,
                                   null=True,
                                   max_length=2000,
                                   verbose_name="Описание товара",
                                   help_text="Можете добавить описание товара")
    author = models.ForeignKey('users.User',
                               verbose_name="Автор объявления",
                               on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Время создания объявления",) # _now_add когда объект создан
    image = models.ImageField(upload_to='ad_images',
                              help_text="Разместите фото для объявления",
                              null=True,
                              blank=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ("-created_at",)

class Comment(models.Model):
    author = models.ForeignKey('users.User',
                               verbose_name="Автор комментария",
                               on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Время создания комментария",)
    text = models.TextField(max_length=1000,
                            verbose_name="Комментарий",
                            help_text="Оставьте свой комментарий здесь",)
    ad = models.ForeignKey(Ad,
                           on_delete=models.CASCADE,
                           verbose_name="Объявление",
                           help_text="Объявление, к которому относится комментарий",)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ("-created_at",)