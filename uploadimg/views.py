# Create your views here.
from django.views import View
from django.shortcuts import render
from uploadimg.forms import ImageForm
from .utils import image_editor
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

class index(View):
    def get(self, request):
        form = ImageForm()
        return render(request, 'uploadimg/index.html', {
            'form': form
            })

    def post(self, request):
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'uploadimg/index.html', {
                'form': form, 
                'img_obj': img_obj
                })

    