from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoorViewSet, home


router = DefaultRouter()
router.register(r'doors', DoorViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', home, name='home'),
]