from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet, UserProfileView, CurrentUserView  # , ChangePasswordView

router = routers.SimpleRouter()
router.register(r'', UserViewSet)
# router.register(r'', CurrentUserView, basename='curr')
# router.register(r'profile/', UserProfileView)


## test ##
urlpatterns = [
    path('', include(router.urls)),
    path('current/', CurrentUserView.as_view(), name='current-user'),
    path('<int:pk>/profile/',
         UserProfileView.as_view(), name='user-profile'),

    # ========================#
    # Create change password
    # ========================#
    
    #path('change-password/', ChangePasswordView.as_view(), name='change-password'),

    # path('login', CustomAuthToken.as_view()),
]
