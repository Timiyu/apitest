from django.shortcuts import render
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views import View
from django.conf import settings
import json


# Create your views here.
class Login(View):
    def get(self, request):
        return render(request, 'web/login.html')

    def post(self, request):
        data = request.body
        data = json.loads(data, encoding='utf8')
        username = data.get('username', '')
        password = data.get('password', '')
        print(username, password)
        return JsonResponse({'success': 'success'}, safe=False)


@login_required(login_url=settings.WEB_LOGIN_URL)
def index(request):
    return render(request, 'web/index.html')
