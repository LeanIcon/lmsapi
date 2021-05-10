from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import serializers, viewsets

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .models import Course_Module
from apps.lessons.views import LessonContentSerializer


class CourseModuleSerializer(serializers.ModelSerializer):
    lessons = LessonContentSerializer(many=True)
    class Meta:
        model = Course_Module
        fields = ('id', 'title', 'description', 'duration', 'course', 
                    'module_number', 'content_one', 'content_two','module_overview', 
                    'resource_url', 'video_url', 'lessons')


# @api_view(["GET", "POST", "PUT"])
# @csrf_exempt
class CourseModuleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Course_Module.objects.all()
    serializer_class = CourseModuleSerializer
