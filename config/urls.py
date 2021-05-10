from django.contrib import admin
from django.urls import path, include, reverse_lazy, re_path
from apps.users import views
from apps.users.views import activate, UserProfileView, CurrentUserView
from apps.lessons.views import LessonStatusViewSet
from django.conf import settings

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from django.contrib.auth import views as auth_views

from apps.practice_test.views import MyQuizListAPI, QuizListAPI, QuizDetailAPI, SaveUsersAnswer, SubmitQuizAPI, QuizResultAPI
    
app_name = 'app.users'

urlpatterns = [
    # Auth Tokens
    path('api-token/', TokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),

    # Admin Dashboard
    path('admin/', admin.site.urls),

    # User data (login and reg, userlist)
    path('api/users/', include('apps.users.urls')), # Get all users

    # Course data
    path('api/courses/', include('apps.courses.urls')), #Get all courses
    # feedback data
    path('api/feedback/', include('apps.feedback.urls')), #Get all courses

    # Course data
    path('api/modules/', include('apps.course_modules.urls')), #Get all courses

    # Lesson data
    path('api/lessons/', include('apps.lessons.urls')), #Get all lessons
    path('api/lesson/completed/', LessonStatusViewSet.as_view(), name='lesson completed'),  # Get all lessons

    # Cert data
    path('api/certificates/', include('apps.certificate.urls')), # Get all certificates

    # Badge data
    path('api/badge/', include('apps.badge.urls')), #Get all badges

    # Account activation
    path('accounts/activate/<slug:uidb64>/<slug:token>/', activate, name='activate'), # Activate your account via email

    # Register a user (unused)
    path('api/register/', include('rest_auth.registration.urls')), # Register an account unused

    # User Update Profile info
    path('api/users/profile/<int:pk>/', UserProfileView.as_view(), name='update profile'),  # Update Profile

    # User Data Info
    path('api/current', CurrentUserView.as_view(), name='current profile'), # Get Current User

    # Forgot password
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

    path('', include('rest_auth.urls')),

    # path('nested_admin', include('nested_admin.urls')),

    # path('api/quiz/', include('apps.practice_test.urls')),

    path("my-quizzes/", MyQuizListAPI.as_view()),
    path("quizzes/", QuizListAPI.as_view()),
    path("save-answer/", SaveUsersAnswer.as_view()),
    re_path(r"quizzes/(?P<slug>[\w\-]+)/$", QuizDetailAPI.as_view()),
    re_path(r"quizzes/(?P<slug>[\w\-]+)/result/$", QuizResultAPI.as_view()),
    re_path(r"quizzes/(?P<slug>[\w\-]+)/submit/$", SubmitQuizAPI.as_view()),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
