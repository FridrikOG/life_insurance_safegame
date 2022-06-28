# from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import PaymentAPIVIEW
from . import views
#from . import views

# Pattern matching
urlpatterns = [
    path('', PaymentAPIVIEW.as_view(), name='createinsurance'),
]
