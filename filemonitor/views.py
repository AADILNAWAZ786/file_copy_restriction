from django.shortcuts import render, redirect
from .models import Config  # assuming Config is the model name
from django.http import HttpResponse

def somewhere_view(request):
    return HttpResponse("You are at the 'somewhere' page!")

def config_view(request):
    config, created = Config.objects.get_or_create(id=1)  # id=1 as a singleton config, or adjust accordingly
    if request.method == 'POST':
        root_folder = request.POST.get('root_folder')
        if root_folder:
            config.root_folder = root_folder
            config.save()
        return redirect('somewhere_view')  # Redirect to the somewhere_view URL
    return render(request, 'filemonitor/config.html', {'config': config})
