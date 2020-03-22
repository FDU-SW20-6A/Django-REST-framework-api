from rest_framework import generics
from . import models
from . import serializers

class PostList(generics.ListAPIView):
    queryset = models.pos.objects.all()
    serializer_class = serializers.positionSerializer
class PostDetail(generics.RetrieveAPIView):
    queryset = models.pos.objects.all()
    serializer_class = serializers.positionSerializer