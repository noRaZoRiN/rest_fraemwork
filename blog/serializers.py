from rest_framework import serializers
from .models import Category, Publication

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['id']

class PublicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created', 'updated']