from django.http import HttpResponse
from django.views import generic

class PostView(generic.View):
    def get(self, request, *args, **kwargs):
         return HttpResponse('<h1 style="font-size: 4em;">hello word</h1>')