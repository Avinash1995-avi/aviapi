from django.urls import path, include
from rest_framework import routers
from .views import BBTView

router = routers.DefaultRouter()
router.register('bigbang',BBTView)

urlpatterns = [
    path('', include(router.urls))
]
