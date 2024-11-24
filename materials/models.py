from django.db import models

from config.settings import AUTH_USER_MODEL


class Course(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название курса",
        help_text="Укажите название курса",
    )
    preview = models.ImageField(
        upload_to="materials/image/",
        verbose_name="Аватарка курса",
        blank=True,
        null=True,
        help_text="Загрузите аватар",
    )
    description = models.CharField(
        max_length=100,
        verbose_name="Описание курса",
        blank=True,
        null=True,
        help_text="Укажите описание курса",
    )

    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец курса", blank=True,
                              null=True, )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название урока",
        help_text="Укажите название урока",
    )
    preview = models.ImageField(
        upload_to="materials/image/",
        verbose_name="Аватарка урока",
        blank=True,
        null=True,
        help_text="Загрузите аватар",
    )
    description = models.CharField(
        max_length=100,
        verbose_name="Описание урока",
        blank=True,
        null=True,
        help_text="Укажите описание урока",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="курс",
        help_text="Укажите курс",
        blank=True,
        null=True,
    )
    video_link = models.URLField(
        verbose_name="Видео урока",
        blank=True,
        null=True,
        help_text="Укажите ссылку на видео урока",
    )

    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец урока", blank=True,
                              null=True, )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.name
