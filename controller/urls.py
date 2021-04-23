"""Robot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from django.urls import path, re_path, include

from .views import *

router = DefaultRouter()
router.register(r'status', StatusView, basename='user')
router.register(r'position', PositionView, basename='user')
router.register(r'package', PackageViewJSON, basename='user')
# router.register(r'rest/package/pos/{position_id}', PackageByPosView, basename='package_by_pos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Controller.as_view(), name='main'),
    path('package/pos/<int:pos_id>', views.PackageView.as_view(), name='package_by_pos'),
    path('/rest/package/pos/<int:pos_id>', views.PackageByPosView.as_view({'get': 'list'}), name='package_by_pos_rest'),
    # path('rest/', include('rest_framework.urls', namespace='rest_framework'))
]
urlpatterns += router.urls
