# from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import PackageView
from . import views
#from . import views

# Pattern matching
urlpatterns = [
    path('', PackageView.as_view(), name=''),
]
