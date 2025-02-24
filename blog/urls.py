from django.urls import path

from .views import CategoryViewSet, CategoryRetrieveupdateDestroyAPIView, PublicationListCreateAPIView, PublicationRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('categories/', CategoryViewSet.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveupdateDestroyAPIView.as_view(), name='category-retrieve-update-destroy'),
    path('publications/', PublicationListCreateAPIView.as_view(), name='publication-list'),
    path('publications/<int:pk>/', PublicationRetrieveUpdateDestroyAPIView.as_view(), name='publication-detail')
]
