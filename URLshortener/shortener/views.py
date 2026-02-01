from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UrlShortener
from .serializers import LongUrlSerializer
from .permissions import CanCreateShortURL
from .utils import base62


class LongUrlApiView(APIView):
    permission_classes = [permissions.IsAuthenticated ,CanCreateShortURL]

    def get_object(self, short_url, user):
        return get_object_or_404(UrlShortener, short_url=short_url, user=user)

    
    def get(self, request, short_url=None):
        if short_url:
            urls = self.get_object(short_url, request.user)
            serializer = LongUrlSerializer(urls)
            return Response(serializer.data)
        else:
            urls = UrlShortener.objects.filter(user=request.user)
            serializer = LongUrlSerializer(urls, many = True)
            return Response(serializer.data)
    
    def post(self, request):
        serializer = LongUrlSerializer(data=request.data, context = {'request': request})
        if serializer.is_valid():
            url_instance = serializer.save()
            if not url_instance.short_url:
                url_instance.short_url = base62(url_instance.id)
                url_instance.save(update_fields = ['short_url'])
            response_serializer = LongUrlSerializer(url_instance)
            return Response(response_serializer.data)
        return Response(serializer.errors)
    

    def put(self, request, short_url):
        urls = self.get_object(short_url, request.user)
        serializer = LongUrlSerializer(urls, data = request.data, partial = True, context = {'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, short_url):
        urls = self.get_object(short_url, request.user)
        urls.delete()
        return Response(status=204)
    

    
def longurl_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
    urls = UrlShortener.objects.all()
    return render(request, 'longurl.html', context={'urls':urls})



class RedirectUrl(APIView):

    def get(self, request, short_url):
        url = get_object_or_404(UrlShortener, short_url=short_url)
        url.clicks += 1
        url.save(update_fields=['clicks']) 
        return redirect(url.original_url)
        

