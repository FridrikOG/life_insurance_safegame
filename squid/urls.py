"""squid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from rest_framework.response import Response

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions



@permission_classes([AllowAny])
class Home(generics.GenericAPIView):

    def get(self, request):
        return Response("squid-django-backend")

# schema_view = get_schema_view(
#     openapi.Info(
#         title="INCOME EXPENSES API",
#         default_version='v1',
#         description="Test description",
#         terms_of_service="https://www.ourapp.com/policies/terms/",
#         contact=openapi.Contact(email="contact@expenses.local"),
#         license=openapi.License(name="Test License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

PREFIX = 'api/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'{PREFIX}', Home.as_view()),
    path(f'{PREFIX}user/', include('user.urls')),
    path(f'{PREFIX}insurance/', include('insurance.urls')),
    path(f'{PREFIX}application/', include('application.urls')),
    path(f'{PREFIX}payment/', include('payment.urls')),
    path(f'{PREFIX}package/', include('package.urls')),
    # path('', schema_view.with_ui('swagger',
    #                              cache_timeout=0), name='schema-swagger-ui'),

    # path('api/api.json/', schema_view.without_ui(cache_timeout=0),
    #      name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc',
    #                                    cache_timeout=0), name='schema-redoc'),

]
