from django.shortcuts import render, redirect
from .models import JobPostingURL
import os
from .forms import URLForm
from .serializer import JobPostingURLSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .royce import *

def submit_url(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('url_list')  # Redirect to a page that shows the list of URLs
    else:
        form = URLForm()
    
    return render(request, 'submit_url.html', {'form': form})

def url_list(request):
    urls = JobPostingURL.objects.all().order_by('-created_at')
    return render(request, 'url_list.html', {'urls': urls})

@api_view(['POST'])
def submit_url_api(request):
    if request.method == 'POST':
        serializer = JobPostingURLSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
def process_urls(request):
    studyPlan = []
    urls = JobPostingURL.objects.all()  # Retrieve all URLs
    getSkillSet
    return render(request, 'process_urls.html', {'urls': urls})