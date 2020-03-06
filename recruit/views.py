from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Application
from .forms import ApplicationForm

# Create your views here.

def main(request):
    art = Application.objects.filter(author=request.user)
    if art:
        return render(request, 'main.html', {'art':art})
    else:
        return render(request, 'main.html')

def new(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            art = form.save(commit=False)
            art.date = timezone.now()
            art.author = request.user
            art.final = False
            art.save()
            return redirect('show')
    else:
        form = ApplicationForm()
        return render(request, 'new.html',{'art':form})

def show(request):
    art = get_object_or_404(Application, author=request.user)
    return render(request, 'show.html', {'art':art})

def edit(request):
    art = get_object_or_404(Application, author=request.user)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, instance=art)
        if form.is_valid():
            art = form.save(commit=False)
            art.date = timezone.now()
            art.save()
            return redirect('show')
    else:
        form = ApplicationForm(instance=art)
        return render(request, 'edit.html',{'art':form})

def submit(request):
    art = get_object_or_404(Application, author=request.user)
    art.final = True
    art.save()
    return render(request, 'show.html', {'art':art})

def delete(request):
    art = get_object_or_404(Application, author=request.user)
    art.delete()
    return render(request, 'main.html')