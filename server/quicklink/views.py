from django.shortcuts import render, redirect, get_object_or_404
from quicklink.models import Redirect
# Create your views here.

def redirect_end(request, key):
    _redirect = get_object_or_404(Redirect, key=key)
    _redirect.register_access(request)
    return redirect(_redirect.url)