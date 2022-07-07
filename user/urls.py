# from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import LoginAPIVIEW, LogOutAPIVIEW, RegisterAPIVIEW, UpdateProfile, PasswordTokenCheckAPIVIEW, RequestPasswordResetEmail, SetNewPasswordAPIView, TestAPIVIEW
from . import views
#from . import views

# Pattern matching
urlpatterns = [
     path('test/', TestAPIVIEW.as_view(), name='test'),
    path('register/', RegisterAPIVIEW.as_view(), name='register'),
    path('login/', LoginAPIVIEW.as_view(), name='login'),
    path('logout/', LogOutAPIVIEW.as_view(), name='logout'),
    path('update/', UpdateProfile.as_view(), name='update'),
    path('delete/', UpdateProfile.as_view(), name='update'),
    path('requestResetEmail/',RequestPasswordResetEmail.as_view(), name='password-reset'),
    path('passwordReset/<uidb64>/<token>/',PasswordTokenCheckAPIVIEW.as_view(), name='password-reset-confirm'),
    path('passwordResetComplete/', SetNewPasswordAPIView.as_view(),name='password-reset-complete')
]
