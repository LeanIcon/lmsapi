from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import serializers, viewsets

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from .models import Lesson, Lesson_Status
from apps.users.models import User
from rest_framework.response import Response


#test
from django.views.generic import View

class LessonContentSerializer(serializers.ModelSerializer):
    completed = serializers.SerializerMethodField()
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'description', 'lesson_number',
                'duration', 'date', 'course_module', 'content_one',
                'content_two', 'content_three',
                'resource_url', 'video_one', 'video_two', 'completed']
        read_only_fields = ['completed']
    
    def get_completed(self, obj):
        try:
            lessonStatus = Lesson_Status.objects.get(user=self.context['request'].user, lesson=obj)
            return lessonStatus.completed
        except Lesson_Status.DoesNotExist:
            return None



# @api_view(["GET", "POST", "PUT"])
# @csrf_exempt
class LessonViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Lesson.objects.all()
    serializer_class = LessonContentSerializer


class LessonStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson_Status
        fields = [
            'lesson', 'user', 'completed'
        ]
 

# @api_view(["GET", "POST", "PUT"])
# @csrf_exempt
class LessonStatusViewSet(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    # queryset = Lesson_Status.objects.all()
    serializer_class = LessonStatusSerializer

    # # @csrf_exempt
    def post(self, request, *args, **kwargs):
        user_id = request.data['user']
        lesson_id = request.data['lesson']

        user = get_object_or_404(User, id=user_id)
        lesson = get_object_or_404(Lesson, id=lesson_id)

        # print('this is test for debug ', user_id, lesson_id)
        obj = Lesson_Status(
            lesson=lesson, user=user, completed=True
        )
        # obj.lesson = lesson
        # obj.user = user
        # obj.completed = True

        obj.save()

        return Response(self.get_serializer(obj).data)

    

