from django.shortcuts import render, redirect
from django.http import HttpResponse
from functools import wraps

# The secret keys to unlock the site.
SECRET_KEYS = ["kunjan", "ponne"]

def key_required(view_func):
    """Decorator to require the correct secret key to access a view."""
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.session.get('is_authenticated', False):
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')
    return _wrapped_view

def launcher(request):
    """The main entry point that hosts the persistent audio and iframe."""
    return render(request, 'core/launcher.html')

def login_view(request):
    if request.method == 'POST':
        key = request.POST.get('key', '').strip().lower()
        if key in SECRET_KEYS:
            request.session['is_authenticated'] = True
            return redirect('home')
        else:
            return render(request, 'core/login.html', {
                'error': 'wrong baby.. enter the name that you call me when we are in love'
            })
    return render(request, 'core/login.html')

def logout_view(request):
    request.session.flush()
    return redirect('login')

@key_required
def home(request):
    return render(request, 'core/home.html')

@key_required
def photos(request):
    return render(request, 'core/photos.html')

@key_required
def game(request):
    return render(request, 'core/game.html')

@key_required
def qa(request):
    return render(request, 'core/qa.html')

@key_required
def letter(request):
    return render(request, 'core/letter.html')
