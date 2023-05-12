from django.urls import path, include
from rest_framework import routers

from dashboard.views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'group', GroupViewSet)

router.register(r'filter', FilterViewSet)
router.register(r'keyword', KeywordViewSet)
router.register(r'alert', AlertViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-path/', include('rest_framework.urls')),
]
