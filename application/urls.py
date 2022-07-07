# from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import ApplicationAPIVIEW,AllApplicationAPIVIEW, WithdrawApplicationAPIVIEW

# Pattern matching
urlpatterns = [
    path('', ApplicationAPIVIEW.as_view(), name='createinsurance'),
    # path('<int:id>/', ApplicationAPIVIEW.as_view(), name='createinsurance'),
    path('withdraw/', WithdrawApplicationAPIVIEW.as_view(), name='createinsurance'),
    path('all/', AllApplicationAPIVIEW.as_view(), name='ins'),

]
