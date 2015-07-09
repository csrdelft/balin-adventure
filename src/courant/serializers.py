from rest_framework import serializers
from .models import *

class CourantEntrySerializer(serializers.ModelSerializer):

  class Meta:
    model = CourantEntry
    read_only_fields = ('user','courant','date_created','date_modified')

class CourantSerializer(serializers.ModelSerializer):

  rendered = serializers.CharField(source='render', read_only=True)
  entries = CourantEntrySerializer(many=True, read_only=True)

  class Meta:
    model = Courant
