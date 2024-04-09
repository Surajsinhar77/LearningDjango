from django.http import HttpResponse, JsonResponse
import requests
from .models import Users
import json
# Create your views here.

def userSignup(request):
    if(request.method == 'POST'):
        userData = json.loads(request.body) # get the data from the request in json
        print(userData['name'])
        return JsonResponse({'message': 'user created'}, status=202, safe=False)
    return JsonResponse({'message': 'invaild request'}, safe=False)