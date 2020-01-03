from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.utils import get_files
from django.contrib.staticfiles.storage import StaticFilesStorage
from django.conf import settings
import os
# Create your views here.
def main(request):
    static_file_storage = StaticFilesStorage()
    dirs = list(static_file_storage.listdir('.'))
    
    for d in dirs:
        if len(d) > 0:
            out = d
    dirs = out

    #print(dirs)
    #files = list(get_files(static_file_storage,location = 'assets'))
    files  = {'dirs':dirs}
    try:
        import os
        #print(os.listdir('..'))
    except:
        pass
    return render(request,'main/main.html',files)
    #return HttpResponse('Hi')

def inner(request,dir_):
    static_file_storage = StaticFilesStorage()
    files = list(static_file_storage.listdir(dir_))
    for f in files:
        if len(f) > 0:
            out = f
    files = f[0]
    fullpath = os.path.join(dir_,files)
    print(fullpath)
    ctx = {'img':fullpath} 
    return render(request,'main/inner.html',ctx)

