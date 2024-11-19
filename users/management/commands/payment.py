import datetime

from django.core.management import BaseCommand

from materials.models import Course, Lesson
from users.models import Payment, User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        User.objects.all().delete()
        Payment.objects.all().delete()

        user1, created = User.objects.get_or_create(email="user1@y.o")
        user2, created = User.objects.get_or_create(email="user2@y.o")
        user3, created = User.objects.get_or_create(email="user3@y.o")

        course1, created = Course.objects.get_or_create(name="Курс 1")
        course2, created = Course.objects.get_or_create(name="Курс 2")
        course3, created = Course.objects.get_or_create(name="Курс 3")

        lesson1, created = Lesson.objects.get_or_create(
            name="Курс 1. Урок 1", course=course1
        )
        lesson2, created = Lesson.objects.get_or_create(
            name="Курс 1. Урок 2", course=course1
        )
        lesson3, created = Lesson.objects.get_or_create(
            name="Курс 1. Урок 3", course=course1
        )
        lesson4, created = Lesson.objects.get_or_create(
            name="Курс 2. Урок 1", course=course2
        )
        lesson5, created = Lesson.objects.get_or_create(
            name="Курс 2. Урок 2", course=course2
        )
        lesson6, created = Lesson.objects.get_or_create(
            name="Курс 3. Урок 1", course=course3
        )

        payment1 = Payment.objects.create(
            user=user1,
            date=datetime.datetime.now().date(),
            amount=100,
            payment_method="cash",
            course_paid=course1,
        )

        payment2 = Payment.objects.create(
            user=user2,
            date=datetime.datetime.now().date(),
            amount=200,
            payment_method="transaction",
            course_paid=course3,
        )

        payment3 = Payment.objects.create(
            user=user3,
            date=datetime.datetime.now().date(),
            amount=500,
            payment_method="transaction",
            lesson_paid=lesson6,
        )

        payment4 = Payment.objects.create(
            user=user3,
            date=datetime.datetime.now().date(),
            amount=700,
            payment_method="cash",
            course_paid=course2,
        )
