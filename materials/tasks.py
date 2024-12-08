from datetime import timedelta

from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from config import settings
from materials.models import Course, Subscription
from users.models import User


@shared_task
def send_update_course(course_id):
    course = Course.objects.get(id=course_id)
    message = f"Новые учебные материалы по курсу '{course.name}"
    users = User.objects.all()
    for user in users:
        subscription = Subscription.objects.filter(course=course, user=user.pk).exists()
        if subscription:
            send_mail(
                subject=f'Новые учебные материалы по курсу "{course}"',
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
            )


@shared_task
def block_user():
    users = User.objects.filter(is_active=True, is_superuser=False, last_login__isnull=False)
    today = timezone.now()
    for user in users:
        if today - user.last_login > timedelta(days=30):
            user.is_active = False
            user.save()
