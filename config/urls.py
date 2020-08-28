"""LMSAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.users import views
from apps.users.views import activate, UserProfileView
from django.conf import settings
# from apps.users.views import ConfirmEmailView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)


from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
    
app_name = 'app.users'

urlpatterns = [
    path('api-token/', TokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),
    path('admin/', admin.site.urls),
    path('api/users/', include('apps.users.urls')), # Get all users
    path('api/courses/', include('apps.courses.urls')), #Get all coursers
    path('api/certificates/', include('apps.certificate.urls')), # Get all certificates
    path('api/badge/', include('apps.badge.urls')), #Get all badges
    path('accounts/activate/<slug:uidb64>/<slug:token>/', activate, name='activate'), # Activate your account via email
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), # Defualt rest authentication
    path('api/register/', include('rest_auth.registration.urls')), # Register an account unused
    path('api/profile/update', UserProfileView.as_view(), name='update profile'), # Update Profile

    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

    path('', include('rest_auth.urls')),


    # path(
    #     'reset_password/',
    #     auth_views.PasswordResetView.as_view(
    #         success_url=reverse_lazy('apps.users:password_reset_done')),
    #     name='reset_password'   
    # ),
    # path(
    #     'reset_password_sent/',
    #     auth_views.PasswordResetDoneView.as_view(),
    #     name='password_reset_done'
    # ),
    # path(
    #     'reset/<uidb64>/<token>/',
    #     auth_views.PasswordResetConfirmView.as_view(
    #         success_url=reverse_lazy('apps.users:password_reset_complete')),
    #     name='password_reset_confirm'
    # ),
    # path(
    #     'reset_password_complete/',
    #     auth_views.PasswordResetCompleteView.as_view(),
    #     name='password_reset_complete'
    # )
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
