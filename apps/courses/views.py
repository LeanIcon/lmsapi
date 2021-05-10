from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import serializers, viewsets

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .models import Course
from apps.course_modules.views import CourseModuleSerializer
from apps.feedback.views import FeedbackSerializer

class CourseLectureSerializer(serializers.ModelSerializer):
    modules = CourseModuleSerializer(many=True)
    feedback = FeedbackSerializer(many=True)
    class Meta:
        model = Course
        fields = (  'id', 'title', 'description', 'date', 'duration',
                    'course_overview', 'resource_url', 'modules', 'feedback',
                    'is_required', 'video_url', 'course_content_one',
                    'course_content_two'
                )


# @api_view(["GET", "POST", "PUT"])
# @csrf_exempt
class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Course.objects.all()
    serializer_class = CourseLectureSerializer
