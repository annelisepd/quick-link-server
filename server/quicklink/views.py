from django.shortcuts import render, redirect, get_object_or_404
from quicklink.models import Redirect
# Create your views here.

def redirect_end(request, key):
    _redirect = get_object_or_404(Redirect, key=key)
    _redirect.register_access(request)
    return redirect(_redirect.url)

def create_redirect(request):
    link = None
    
    if request.method == 'POST':
        url = request.POST.get('url')
        if url:
            redirect = Redirect(url=url)
            redirect.save()
            link = request.build_absolute_uri('/') + redirect.key
    
    return render(request, 'create_redirect.html', {'link': link})
