from rest_framework import serializers
from .models import Edata


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edata
        fields = ('end_year', 'intensity', 'sector', 'topic','insight','url', 'region', 'start_year','impact','added','published','country','relevance','pestle','source','title','likelihood')