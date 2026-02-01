from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UrlShortener
from .serializers import LongUrlSerializer
from .permissions import CanCreateShortURL


class LongUrlApiView(APIView):
    permission_classes = [permissions.IsAuthenticated ,CanCreateShortURL]

    
    def get(self, request):
        urls = UrlShortener.objects.all()
        serializer = LongUrlSerializer(urls, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = LongUrlSerializer(data=request.data, context = {'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
def longurl_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
    urls = UrlShortener.objects.all()
    return render(request, 'longurl.html', context={'urls':urls})


# class CreateshortUrl(APIView):
#     permission_classes = [permissions.IsAuthenticated, CanCreateShortURL]

#     def get(self, request):
#         urls = UrlShortener.objects.all()
#         serializer = ShortUrlSerializer(urls, many=True)
#         return Response(serializer.data)


class RedirectUrl(APIView):

    def get(self, request, short_url):
        url = get_object_or_404(UrlShortener, short_url=short_url)
        return redirect(url.original_url)
        

