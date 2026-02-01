from rest_framework import serializers
from shortener.models import UrlShortener

class LongUrlSerializer(serializers.ModelSerializer):
    short_url = serializers.CharField(required=False, allow_blank=True) 
    class Meta:
        model = UrlShortener
        fields = ['user','original_url', 'short_url']

# class ShortUrlSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UrlShortener
#         fields = ['user','original_url','short_url']

