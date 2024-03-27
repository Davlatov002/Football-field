from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Foodballfield, Bron
from drf_yasg.utils import swagger_auto_schema
from .serializer import FoodballfieldSerialazer, BronSerialazer, BronCreateSerializer, UpdateBronSerializer, UpdatefoodballfildSerializer, FillterSerializer
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import PermissionDenied
from datetime import datetime
import re, math
from django.http import JsonResponse
from django.db.models import Q
from datetime import datetime


@swagger_auto_schema(methods='GET')
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_all_foodballfild(request):
    if request.method == 'GET':
        
        foodballfilds = Foodballfield.objects.all()
        serializer = FoodballfieldSerialazer(foodballfilds, many=True)
        return Response({"Foodballfield":serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_footballfild_id(request, pk):
    try:
        fod = Foodballfield.objects.get(id=pk)
    except Foodballfield.DoesNotExist:
        return Response({'message': "Bunday id li foydalanuvchi topilmadi"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = FoodballfieldSerialazer(fod, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_footballfild_owner(request):

    if request.user.roles == 'USER':
        raise PermissionDenied("Sizning ro'lingiz uchun ruxsat etilmagan")
    
    user = request.user.id
    try:
        fod = Foodballfield.objects.filter(owner=user)
    except Foodballfield.DoesNotExist:
        return Response({'message': "Bunday id li foydalanuvchi topilmadi"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = FoodballfieldSerialazer(fod, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(method='POST', request_body=FoodballfieldSerialazer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_foodballfield(request):
    if request.method == 'POST':
        if request.user.roles == 'USER':
            raise PermissionDenied("Sizning ro'lingiz uchun ruxsat etilmagan")
        
        serializer = FoodballfieldSerialazer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='PUT', request_body=UpdatefoodballfildSerializer)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_foodballfield(request, pk):
    try:
        foodballfield = Foodballfield.objects.get(pk=pk)
    except Foodballfield.DoesNotExist:
        return Response({'message': "Bunday id li Foodballfield topilmadi"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':

        if request.user.roles == 'USER':
            raise PermissionDenied("Sizning ro'lingiz uchun ruxsat etilmagan")
        
        serializer = UpdatefoodballfildSerializer(foodballfield, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_foodballfield(request, pk):
    try:
        foodballfield = Foodballfield.objects.get(pk=pk)
    except Foodballfield.DoesNotExist:
        return Response({'message': "Bunday id li Foodballfield topilmadi"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':

        if request.user.roles == 'USER':
            raise PermissionDenied("Sizning ro'lingiz uchun ruxsat etilmagan")
        
        foodballfield.delete()
        return Response({'message': "Foodballfield muvofaqiyatli o'chirildi"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_bron_id(request, pk):
    try:
        bron = Bron.objects.get(id=pk)
    except Bron.DoesNotExist:
        return Response({'message': "Bunday id li foydalanuvchi topilmadi"}, status=status.HTTP_404_NOT_FOUND)
    serializer = BronSerialazer(bron, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(methods='GET')
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_all_brons(request):
    if request.method == 'GET':
        if request.user.roles == 'USER' or request.user.roles == 'OWNER FIELD':
            raise PermissionDenied("Sizning ro'lingiz uchun ruxsat etilmagan")
        brons = Bron.objects.all()
        serializer = BronSerialazer(brons, many=True)
        return Response({"Brons":serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_bron_user(request):
    
    user = request.user.id
    try:
        fod = Bron.objects.filter(user_id=user)
    except Foodballfield.DoesNotExist:
        return Response({'message': "Bunday id li foydalanuvchi topilmadi"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = FoodballfieldSerialazer(fod, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_bron_owner(request, pk):

    if request.user.roles == 'USER':
            raise PermissionDenied("Sizning ro'lingiz uchun ruxsat etilmagan")

    try:
        fod = Bron.objects.filter(foodballfield_id=pk)
    except Foodballfield.DoesNotExist:
        return Response({'message': "Bunday id li bron topilmadi"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = FoodballfieldSerialazer(fod, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(method='POST', request_body=BronCreateSerializer)
@api_view(['POST'])
@permission_classes([AllowAny])
def create_bron(request):
    if request.method == 'POST':
        serializer = BronCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='PUT', request_body=UpdateBronSerializer)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_bron(request, pk):
    try:
        user = Bron.objects.get(pk=pk)
    except Bron.DoesNotExist:
        return Response({'message': "Bunday id li foydalanuvchi topilmadi"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        if request.user.roles == 'USER':
            raise PermissionDenied("Sizning ro'lingiz uchun ruxsat etilmagan")
        
        serializer = UpdateBronSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@swagger_auto_schema(method='DELETE', operation_description="O'chirmoqchi bo'lgan Bron ID sini kirting")
@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def bron_delete(request, pk):
    if request.method == 'DELETE':
        if request.user.roles == 'USER':
            raise PermissionDenied("Sizning ro'lingiz uchun ruxsat etilmagan")
        try:
            bron = Bron.objects.get(id=pk)
        except:
            return Response({'message': "Bunaqa bron yo'q" },status=status.HTTP_400_BAD_REQUEST)
        bron.delete()
        return Response({'message':"muvofaqiyatli o'chirildi"},status=status.HTTP_200_OK)
    else:
        return Response({'message': "Xatoolik yuzaga keldi"},status=status.HTTP_400_BAD_REQUEST)
    

@swagger_auto_schema(method='POST', request_body=FillterSerializer)
@api_view(['POST'])
def filter_stadium(request):

    if request.user.roles == 'OWNER FIELD':
        raise PermissionDenied("Sizning ro'lingiz uchun ruxsat etilmagan")

    start_time = request.data.get('start_time')
    end_time = request.data.get('end_time')
    x = request.data.get('x')
    y =request.data.get('y')

    try:
        start_time = datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%SZ')
        end_time = datetime.strptime(end_time, '%Y-%m-%dT%H:%M:%SZ')
    except ValueError:
        return JsonResponse({'error': 'Invalid date format'}, status=status.HTTP_400_BAD_REQUEST)

    available_fields = set(map(lambda x: x.foodballfield_id.id, Bron.objects.exclude(Q(start_time__lte=start_time, end_time__gte=end_time))))
    addresses = [i for i in Foodballfield.objects.all() if i.id in available_fields or i.id not in map(lambda x : x.foodballfield_id.id,Bron.objects.all())]

    sorted_addresses = sorted(addresses, key=lambda a: math.sqrt((x - float(a.address.split(",")[0]))**2 + (y - float(a.address.split(",")[1]))**2))

    serialized_fields = FoodballfieldSerialazer(sorted_addresses, many=True)
    return JsonResponse(serialized_fields.data, safe=False, status=status.HTTP_200_OK)
