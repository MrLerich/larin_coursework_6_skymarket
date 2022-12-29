from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from users.managers import UserManager, UserRoles


class User(AbstractBaseUser):
    first_name = models.CharField(verbose_name='Имя',
                                  help_text="Введите Имя, макс 200 символов",
                                  max_length=200,
                                  blank=True)
    last_name = models.CharField(verbose_name='Фамилия',
                                 help_text="Введите Фамилию, макс 200 символов",
                                 max_length=200,
                                 blank=True)
    phone = PhoneNumberField(verbose_name='Номер телефона', null=False, blank=False)
    email = models.EmailField(unique=True, help_text="Укажите ваш email", )
    role = models.CharField(max_length=3, choices=UserRoles.choices, default=UserRoles.USER)
    image = models.ImageField(upload_to='avatars', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perm(self, app_label):
        return self.is_admin

    # эта константа определяет поле для логина пользователя
    USERNAME_FIELD = 'email'

    # эта константа содержит список с полями,
    # которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    # для корректной работы нам также необходимо
    # переопределить менеджер модели пользователя

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
