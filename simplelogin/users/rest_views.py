from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def register_user(request):
    data = request.data
    user = User.objects.create_user(password=data["password"], email=data["email"])
    return Response({"Success": "User Registered"})
