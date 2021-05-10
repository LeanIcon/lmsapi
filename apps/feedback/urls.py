from django.urls import path, include
from rest_framework import routers
from .views import FeedbackViewSet

router = routers.DefaultRouter()
router.register(r'', FeedbackViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
