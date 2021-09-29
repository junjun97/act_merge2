from django.shortcuts import render
from django.contrib.auth.models import User
from settings.update_json import *
# Create your views here.
def inform(request):
    userinfo = User.objects.get(username=request.user.username)
    return render(request, 'inform.html', {'userinfo': userinfo, 'user_id': user_id, })
