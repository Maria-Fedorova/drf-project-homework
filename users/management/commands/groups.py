from django.contrib.auth.models import Group
from django.core.management import BaseCommand

from materials.models import Course, Lesson
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        User.objects.all().delete()
        Course.objects.all().delete()
        Lesson.objects.all().delete()

        user1, created = User.objects.get_or_create(email="user1@y.o")
        user2, created = User.objects.get_or_create(email="user2@y.o")
        user3, created = User.objects.get_or_create(email="user3@y.o")

        user1.set_password("123qwe")
        user1.save()
        user2.set_password("123qwe")
        user2.save()
        user3.set_password("123qwe")
        user3.save()

        course1, created = Course.objects.get_or_create(name="Курс 1", owner=user1)
        course2, created = Course.objects.get_or_create(name="Курс 2", owner=user2)
        course3, created = Course.objects.get_or_create(name="Курс 3", owner=user3)

        lesson1, created = Lesson.objects.get_or_create(
            name="Курс 1. Урок 1", course=course1, owner=user1
        )
        lesson2, created = Lesson.objects.get_or_create(
            name="Курс 1. Урок 2", course=course1, owner=user1
        )
        lesson3, created = Lesson.objects.get_or_create(
            name="Курс 1. Урок 3", course=course1, owner=user1
        )
        lesson4, created = Lesson.objects.get_or_create(
            name="Курс 2. Урок 1", course=course2, owner=user2
        )
        lesson5, created = Lesson.objects.get_or_create(
            name="Курс 2. Урок 2", course=course2, owner=user2
        )
        lesson6, created = Lesson.objects.get_or_create(
            name="Курс 3. Урок 1", course=course3, owner=user3
        )
        moderators_group, created = Group.objects.get_or_create(name="moderators")
        user1.groups.add(moderators_group)
