from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ProjectViewSet

# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'projects', ProjectViewSet, basename='project')

urlpatterns = [
    path('', include(router.urls)),  # Includes all standard CRUD routes
    path('projects/assigned/', ProjectViewSet.as_view({'get': 'assigned'}), name='assigned-projects'),
    

]
