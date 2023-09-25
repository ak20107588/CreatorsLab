from django.shortcuts import render,redirect
from .models import*
from django.contrib import messages

# Create your views here.

def dashboard(request):
    if request.session.has_key('is_logged'):
        return render(request,'dashboard.html')
    messages.warning(request,'Please Login!')
    return redirect('/')

def fileupload(request):
    if request.session.has_key('is_logged'):
        return render(request,'fileupload.html')
    messages.warning(request,'Please Login!')
    return redirect('/')

def uploadfile(request):
    if request.session.has_key('is_logged'):
        FileUpload=(request.FILES['fileInput'])

        data={
            'FileUpload':FileUpload
        }

        a=UploadFile(FileUpload=FileUpload)
        a.save()

        messages.success(request,'File Uploaded Successfully')
        return render(request,'fileupload.html')
    messages.warning(request,'Please Login!')
    return redirect('/')
