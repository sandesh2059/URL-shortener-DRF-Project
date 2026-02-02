from rest_framework import serializers
from shortener.models import UrlShortener

class LongUrlSerializer(serializers.ModelSerializer):
    short_url = serializers.CharField(required=False, allow_blank=True) 
    class Meta:
        model = UrlShortener
        fields = ['id', 'user','original_url', 'short_url', 'created_at', 'clicks']
        read_only_fields = ['id','user', 'created_at', 'clicks']
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)



