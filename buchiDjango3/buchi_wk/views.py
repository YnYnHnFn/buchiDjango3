from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

# Create your views here.

def index(request):
    return render(request, 'buchi_wk/index.html' )


def try_bootstrap(request):
    return render(request, 'buchi_wk/try_bootstrap.html' )

def try_font(request):
    return render(request, 'buchi_wk/try_font.html' )

def try_fontawesome(request):
    return render(request, 'buchi_wk/try_fontawesome.html' )

