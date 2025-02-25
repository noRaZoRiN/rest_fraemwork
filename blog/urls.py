from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, CategoryRetrieveupdateDestroyAPIView, PublicationListCreateAPIView, PublicationRetrieveUpdateDestroyAPIView, CategoryFilter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # path('categories/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category-list-create'),
    # path('categories/<int:pk>/', CategoryRetrieveupdateDestroyAPIView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='category-retrieve-update-destroy'),
    path('publications/', PublicationListCreateAPIView.as_view(), name='publication-list'),
    path('publications/<int:pk>/', PublicationRetrieveUpdateDestroyAPIView.as_view(), name='publication-detail'),
    path('categories/filter/', CategoryFilter.as_view(), name='category-filter'),
    path('api/', include(router.urls)),
]
