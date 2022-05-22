# Create your views here.
from django.views import View
from django.shortcuts import render
from . models import Image



class index(View):
    def get(self, request):
        return render(request, 'uploadimg/index.html', {
            })

    def post(self, request):
        form = request.FILES.get('image')
        image = Image(image=form)
        image.save()
        return render(request, 'uploadimg/index.html', {
            'img_obj': image.image
        })

    