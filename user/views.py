from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import CustomUser
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import CustomTokenObtainPairSerializer, CostomuserSerializer,UpdateCostomUserSerializer, UserCreateSerializer
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth.hashers import make_password

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

@swagger_auto_schema(method='POST', request_body=UserCreateSerializer)
@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    if request.method == 'POST':
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():

            validated_data = serializer.validated_data
            validated_data['password'] = make_password(validated_data['password'])

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='PUT', request_body=UpdateCostomUserSerializer)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request):
    id = request.data.id
    try:
        user = CustomUser.objects.get(id=id)
    except CustomUser.DoesNotExist:
        return Response({'message': "Bunday id li foydalanuvchi topilmadi"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UpdateCostomUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request):
    id = request.data.id
    try:
        user = CustomUser.objects.get(id=id)
    except CustomUser.DoesNotExist:
        return Response({'message': "Bunday id li foydalanuvchi topilmadi"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        user.delete()
        return Response({'message': "Foydalanuvchi muvofaqiyatli o'chirildi"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):
    id = request.user.id
    user = CustomUser.objects.get(id=id)
    serializer = CostomuserSerializer(user, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_user(request):

    if request.user.roles == 'USER' or request.user.roles == 'OWNER FIELD':
        raise PermissionDenied("Sizning ro'lingiz uchun ruxsat etilmagan")
    
    profiles = CustomUser.objects.all()
    serializer = CostomuserSerializer(profiles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

