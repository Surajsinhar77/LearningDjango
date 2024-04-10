from rest_framework.decorators import api_view
import requests
from .models import Users
from rest_framework.response import Response
from .serielizer import UserSerializer , PostSerializer
import json
import hashlib
from rest_framework.authtoken.models import Token
from rest_framework import status
# Create your views here.


@api_view(['POST'])
def sign_up(req):
    try:
        data = req.data
        email = data['email']
        password = data['password']
        name = data['name']
        # use serializer to validate the data
        # we need to hash the password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        data['password'] = hashed_password
        serializer = UserSerializer(data=data)
        if Users.objects.filter(email=email).exists():
            return Response({'message': 'User already exists'})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully'})
        # throw exception in the else
        else:
            raise Exception('User not created successfully')
    except Exception as e:
        return Response({'message': str(e)})


@api_view(['POST'])
def login(req):
    try:
        data = req.data
        email = data['email']
        password = data['password']
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
        user = Users.objects.filter(email=email).first()
        if user.password != hashed_password:
            raise Exception('invalid password')
        if user:
            #token, created = Token.objects.get_or_create(user=user)
            # print(token.key)
            token = 'Token ' + str(user.id)
            return Response({'message': 'Login successful', 'token': token})
        else:
            raise Exception('Login not successful')
    except Exception as e:
        print(e)
        return Response({'message': str(e)})
    

@api_view(['GET'])
def get_user(req):
    try:
        if req.user.is_authenticated:  # Add authorization check
            users = Users.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        else:
            return Response({'message': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response({'message': str(e)})
    

@api_view(['POST'])
def create_post(req):
    try:
        data = req.data
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Post created successfully'})
        # throw exception in the else
        else:
            raise Exception('Post not created successfully')
    except Exception as e:
        return Response({'message': str(e)})