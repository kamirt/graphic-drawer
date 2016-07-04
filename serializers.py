from . models import Upload
from rest_framework import serializers


class UploadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Upload
        fields = ('x', 'y')

