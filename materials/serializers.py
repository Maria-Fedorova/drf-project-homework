from rest_framework import serializers
from rest_framework.fields import URLField
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Course, Lesson, Subscription
from materials.validators import validate_video_link


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    video_link = URLField(validators=[validate_video_link])

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    count_lesson = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True, source='lesson_set')
    subscribers = serializers.SerializerMethodField(read_only=True)

    def get_count_lesson(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_subscribers(self, course):
        user = self.context["request"].user
        return Subscription.objects.filter(user=user).filter(course=course).exists()

    class Meta:
        model = Course
        fields = ("name", "description", "preview", "lessons", "count_lesson", "subscribers",)


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
