from django.urls import path, include, re_path
from rest_framework import routers
from .views import LessonViewSet, LessonStatusViewSet

router = routers.DefaultRouter()
router.register(r'', LessonViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("completed/", LessonStatusViewSet.as_view()),
]
