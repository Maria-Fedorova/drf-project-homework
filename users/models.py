from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту"
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        blank=True,
        null=True,
        help_text="Введите номер телефона",
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        verbose_name="Аватар",
        blank=True,
        null=True,
        help_text="Загрузите аватар",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Payment(models.Model):
    PAYMENT_METHOD = [("Cash", "cash"), ("Transaction", "transaction")]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Платеж",

        blank=True,
        null=True,

    )

    date = models.DateField(
        verbose_name="Дата платежа",
        blank=True,
        null=True,
    )

    lesson_paid = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name="Оплаченный урок",
        blank=True,
        null=True,
    )

    course_paid = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Оплаченный курс",
        blank=True,
        null=True,
    )

    amount = models.PositiveIntegerField(default=0, verbose_name="Стоимость")

    payment_method = models.CharField(
        choices=PAYMENT_METHOD, default="Cash", verbose_name="Способ оплаты"
    )

    session_id = models.CharField(max_length=255,
                                  verbose_name="ID сессии",
                                  blank=True,
                                  null=True, )
    link = models.URLField(max_length=400,
                                      verbose_name="Ссылка на оплату",
                                      blank=True,
                                      null=True, )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return f"{self.user} - {self.amount}"
