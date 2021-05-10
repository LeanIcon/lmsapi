from django.urls import path, include
from rest_framework import routers
from .views import CourseModuleViewSet

router = routers.DefaultRouter()
router.register(r'', CourseModuleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
