from django.urls import path
from zchess2.views import home
urlpatterns = [path('', home),]