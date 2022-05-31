from django.views import View
from django.shortcuts import render, redirect
from . models import ImageModel
from .utils import image_editor



class index(View):
    def get(self, request):
        return render(request, 'uploadimg/index.html', {
            })

    def post(self, request):
        image_front = request.FILES.get('image_front')
        image_back = request.FILES.get('image_back')
        color = request.POST.get('tshirt_color')
        position = request.POST.get('position')

        if image_front == None and image_back == None:
            return redirect('index')
        
        img = ImageModel(img_front=image_front, img_back=image_back)
        img.save(image_front, image_back, color, position)
        print(img.img_front)
        return render(request, 'uploadimg/index.html', {
            'img_front': img.img_front , 'img_back': img.img_back
        })