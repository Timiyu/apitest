from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apitest.settings import WEB_LOGIN_URL

# Create your views here.

@login_required(login_url=WEB_LOGIN_URL)
def index(request):
    return render(request, 'web/index.html')