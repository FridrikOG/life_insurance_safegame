# from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import CreateApplicationAPIVIEW
from . import views
#from . import views


# Pattern matching
urlpatterns = [
    path('', CreateApplicationAPIVIEW.as_view(), name='createinsurance'),
    # path('update/', LogOutAPIVIEW.as_view(), name='logout'),
    # path('delete/', UpdateProfile.as_view(), name='update'),
]
