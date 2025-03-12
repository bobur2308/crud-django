from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, home

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', home, name='home'),  # Home page at "/"
    path('api/', include(router.urls)),  # API routes under "/api/"
]
