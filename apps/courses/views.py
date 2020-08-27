from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import serializers, viewsets

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .models import Course


class CourseLectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'date', 'duration',
                    'resource1_url', 'resource2_url', 'resource3_url',
                    'is_required', 'video1_url', 'video2_url' , 'video3_url',
                    'course_content_one', 'course_content_two',
                    'course_content_three', 'course_content_four',)


# @api_view(["GET", "POST", "PUT"])
# @csrf_exempt
@permission_classes([IsAuthenticated])
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseLectureSerializer
