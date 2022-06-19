# from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import CreateAPIVIEW
from . import views
#from . import views

# Pattern matching
urlpatterns = [
    path('', CreateAPIVIEW.as_view(), name='createinsurance'),
    # path('update/', LogOutAPIVIEW.as_view(), name='logout'),
    # path('delete/', UpdateProfile.as_view(), name='update'),
]
