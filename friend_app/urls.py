from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('post',views.PostViewSet,basename='post')

urlpatterns  = router.urls