from rest_framework.viewsets import ModelViewSet
from requests import Response
from rest_framework import viewsets, permissions, generics
from rest_framework.exceptions import PermissionDenied
from rest_framework.mixins import ListModelMixin
from rest_framework.views import APIView

from .models import Category, Publication
from .serializers import CategorySerializer, PersonSerializer, PublicationSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveupdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PublicationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Publication.objects.filter(is_archived=False)
    serializer_class = PublicationSerializer
    Permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PublicationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        if self.get_object().user != self.request.user:
            raise PermissionDenied("You do not have permission to edit this publication.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise PermissionDenied("You do not have permission to delete this publication.")
        instance.delete()


class CategoryFilter(APIView):
    def get(self, request):
        name = request.query_params.get('name', None)
        if name:
            categories = Category.objects.filter(name__icontains=name)
        else:
            categories = Category.objects.all()

        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
