# -*- coding:utf-8 -*-
from rest_framework import serializers
from . import models
class positionSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','locationName','longitude','latitude','infectionTime','createdTime','changedTime',)
        model=models.pos