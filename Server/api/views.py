from django.shortcuts import render
from django.http import JsonResponse
from .serializers import UserSerializer, CategorySerializer, ColorSerializer, IconSerializer, TaskSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import Categories, Colors, Icons, Tasks
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.utils import timezone
import datetime
from .static import *

@api_view(['GET', 'POST'])
@permission_classes([])
@authentication_classes([])
def ping(request):
    if request.method == "GET":
        return Response({"request" : "pong"})
    elif request.method == "POST":
        return Response({"request" : "pong post"})

@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def registerUser(request):
    userSerializer = UserSerializer(data=request.data)
    if userSerializer.is_valid():
        userSerializer.save()
        response = userSerializer.data
        response["code"] = CREATE_SUCCESS
        return Response(response, status=status.HTTP_201_CREATED)
    response = userSerializer.errors
    response["code"] = BAD_REQUEST
    return Response(response, status=status.HTTP_201_CREATED)

class CategoryList(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        user_id = request.user.id
        categories = Categories.objects.filter(user__id=user_id)
        cattegorySerializer = CategorySerializer(categories, many=True)
        return Response(cattegorySerializer.data)
    
    def create(self, request, *args, **kwargs):
        data = request.data
        data["user"] = request.user.id
        catSerializer = CategorySerializer(data=data)
        if catSerializer.is_valid():
            cat = catSerializer.save()
            return Response(catSerializer.data, status=status.HTTP_201_CREATED)
        return Response(catSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    
class ColorList(generics.ListCreateAPIView):
    queryset = Colors.objects.all()
    serializer_class = ColorSerializer

class IconList(generics.ListCreateAPIView):
    queryset = Icons.objects.all()
    serializer_class = IconSerializer
    
class TaskList(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    
    def list(self, request, *args, **kwargs):
        category = request.query_params.get("category")
        user = request.user.id
        if category is None:
            return Response({'error' : 'Bad request'}, status=status.HTTP_400_BAD_REQUEST)
        tasks = Tasks.objects.filter(categoryId=category, user=user)
        taskSerializer = TaskSerializer(tasks, many=True)
        return Response(taskSerializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        data = request.data
        data["user"] = request.user.id
        print(data, flush=True)
        taskSerializer = TaskSerializer(data=data)
        
        if taskSerializer.is_valid():
            taskSerializer.save()
            return Response(taskSerializer.data, status=status.HTTP_201_CREATED)
        return Response(taskSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TaskDeital(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def get_all_completed_tasks(request):
    user = request.user.id
    tasks = Tasks.objects.filter(user=user, isCompleted=True)
    taskSerializer = TaskSerializer(tasks, many=True)
    return Response(taskSerializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def get_all_tasks_today(request):
    user = request.user.id
    today_min = datetime.combine(timezone.now().date(), datetime.today().time().min)
    today_max = datetime.combine(timezone.now().date(), datetime.today().time().max)
    tasks = Tasks.objects.filter(dateTimeDone__range=(today_min, today_max))
    taskSerializer = TaskSerializer(tasks, many=True)
    return Response(taskSerializer.data, status=status.HTTP_200_OK)
    