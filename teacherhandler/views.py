import json
import re

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from conversationhandler.models import Conversation
from conversationhandler.serializers import ConversationSerializer
from teacherhandler.models import TeacherUser
from teacherhandler.serializers import TeacherUserSerializer


def teacherRobot(request):
    pass

@csrf_exempt
def teadentLogin(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('inputValue_teacher_username', '')
            password = data.get('inputValue_teacher_pwd', '')
            teacher_user = TeacherUser.objects.get(username=username)
            if password == teacher_user.password:
                teacher_id = teacher_user.teacher_id
                return JsonResponse({'message': 'Login successful','username':username,'teacher_id':teacher_id})
            else:
                return JsonResponse({'message': 'Login failed'}, status=401)
        except Exception as e:
            return JsonResponse({'message': 'Error during login', 'error': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)

@api_view(['GET'])
@csrf_exempt
def get_teacherUser_data(request,teacher_id):
    try:
        teacher_user = TeacherUser.objects.get(teacher_id=teacher_id)
        serializer = TeacherUserSerializer(teacher_user)
        return Response(serializer.data)
    except TeacherUser.DoesNotExist:
        return Response({'error':'TeacherUser not found'},status=404)

@api_view(['POST'])
def update_teacherUser_data(request,teacher_id):
    try:
        teacher_user = TeacherUser.objects.get(teacher_id=teacher_id)
    except TeacherUser.DoesNotExist:
        return Response("User not found",status=status.HTTP_404_NOT_FOUND)

    serializer = TeacherUserSerializer(teacher_user,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("User information updated successfully!",status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
@api_view(['POST'])
def update_teacherUser_avatar(request,teacher_id):
    try:
        teacher_user = TeacherUser.objects.get(teacher_id=teacher_id)
        def extract_number_from_string(input_string):
            # 使用正则表达式匹配数字部分
            matches = re.findall(r'\d+', input_string)

            # 提取匹配到的第一个数字
            if matches:
                number = matches[0]
                return number
            else:
                return None
        teacher_user.teacher_avatar = "https://api.dicebear.com/7.x/miniavs/svg?seed="+extract_number_from_string(str(request.data))
        teacher_user.save()
        return Response("User Avatar updated successfully!",status=status.HTTP_200_OK)

    except TeacherUser.DoesNotExist:
        return Response("User not found",status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def teacherRegister(request):
    serializer = TeacherUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@require_http_methods(["GET"])
def getAllRobots(request,teacher_id):
    robots = Conversation.objects.filter(user_type="teacher",user_id=teacher_id)
    serializer = ConversationSerializer(robots, many=True)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
