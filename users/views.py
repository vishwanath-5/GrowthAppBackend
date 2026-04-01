from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import status

User = get_user_model()  # ✅ FIX

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):

    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if not username or not password:
        return Response({"error": "Username and password required"}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({"error": "User already exists"}, status=400)

    User.objects.create_user(
        username=username,
        password=password,
        email=email
    )

    return Response({"message": "User created successfully"})