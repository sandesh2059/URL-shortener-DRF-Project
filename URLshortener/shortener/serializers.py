from rest_framework import serializers
from shortener.models import UrlShortener

class LongUrlSerializer(serializers.ModelSerializer):
    short_url = serializers.CharField(required=False, allow_blank=True) 
    class Meta:
        model = UrlShortener
        fields = ['user','original_url', 'short_url', 'created_at', 'clicks']
        read_only_fields = ['created_at', 'clicks']



