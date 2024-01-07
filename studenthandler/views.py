import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from studenthandler.models import StudentUser
from studenthandler.serializers import StudentUserSerializer


# Create your views here.
def studentRobot(request):
    pass

@csrf_exempt
def studentLogin(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('inputValue_stu_phone', '')
            password = data.get('inputValue_stu_pwd', '')
            student_user = StudentUser.objects.get(username=username)
            print("student_user:",student_user.password)
            if password == student_user.password:
                student_id = student_user.student_id
                return JsonResponse({'message': 'Login successful','username':username,'student_id':student_id})
            else:
                return JsonResponse({'message': 'Login failed'}, status=401)
        except Exception as e:
            return JsonResponse({'message': 'Error during login', 'error': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)


@api_view(['GET'])
@csrf_exempt
def get_studentUser_data(request,student_id):
    try:
        student_user = StudentUser.objects.get(student_id = student_id)
        serializer = StudentUserSerializer(student_user)
        return Response(serializer.data)
    except StudentUser.DoesNotExist:
        return Response({'error':'StudentUser not found'},status=404)

@api_view(['POST'])
def update_studentUser_data(request,student_id):
    try:
        student_user = StudentUser.objects.get(student_id=student_id)
    except StudentUser.DoesNotExist:
        return Response("User not found.", status=status.HTTP_404_NOT_FOUND)

    serializer = StudentUserSerializer(student_user,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("User information updated sucessfully!",status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def studentRegister(request):
    serializer = StudentUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)