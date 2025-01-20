from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, PublicationListCreateAPIView, PublicationRetrieveUpdateDestroyAPIView

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('categories/<int:pk>/', include('rest_framework.urls', namespace='rest_framework')),
    path('publications/', PublicationListCreateAPIView.as_view(), name='publication-list'),
]