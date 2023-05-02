from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@csrf_exempt
@api_view(('POST',))
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'})
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Login or password may be incorrect'})
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=status.HTTP_200_OK)
