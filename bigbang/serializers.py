from rest_framework import serializers
from .models import BigBangTheory

class BBTSerializer(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = BigBangTheory
        fields = ('name', 'url','desgination', 'performance')
