from django.urls import path
from .views import LongUrlApiView, longurl_list, RedirectUrl
from . import views

urlpatterns = [
    path('longurl/', views.LongUrlApiView.as_view(), name='longurl'),
    path('longurl-list/', views.longurl_list, name='longurl-list'),
    path('<str:short_url>/', views.RedirectUrl.as_view(), name='redirect-url'),
    path('longurl/<str:short_url>/', views.LongUrlApiView.as_view(), name='longurldetail'),
]