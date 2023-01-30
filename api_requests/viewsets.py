from rest_framework import viewsets
from . import models 
from . import serializers 

class ProfileViewset(viewsets.ModelViewSet):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer