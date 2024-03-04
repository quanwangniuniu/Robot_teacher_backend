from django.http import JsonResponse
from django.shortcuts import render
import random
import json
from http import HTTPStatus
from dashscope import Generation
from django.views.decorators.csrf import csrf_exempt
import dashscope
from dashscope.api_entities.dashscope_response import Role
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Conversation,Message
from .serializers import ConversationSerializer,MessageSerializer
dashscope.api_key = "sk-ed6d4a77b7b343679f7860466e562247"

@csrf_exempt
def conversation_view(request,robot_id,robot_role):
    if request.method == 'POST':
        try:
            data = request.body.decode('utf-8')
            messages = [{'role':Role.SYSTEM,'content':robot_role}]
            messages.append({'role':Role.USER,'content':data})
            message = Message()
            message.conversation_id = robot_id
            message.message_content = data
            message.message_type = 'right' # 用户信息为right
            message.save()
            response = Generation.call(
                'qwen-max',
                messages=messages,
                seed = random.randint(1,10000),
                result_format = 'message',
            )

            if response.status_code == HTTPStatus.OK:
                robot_response = response.output.choices[0]['message']['content']
                robot_message = Message()
                robot_message.message_content = robot_response
                robot_message.message_type = 'left' # 机器人回复为left
                robot_message.conversation_id = robot_id
                robot_message.save()
                messages.append({'role': response.output.choices[0]['message']['role'],
                                 'content': response.output.choices[0]['message']['content']})
                return JsonResponse({'response': robot_response, 'messages': messages})
            else:
                return JsonResponse({
                                        'error': f'Request id: {response.request_id}, Status code: {response.status_code}, error code: {response.code}, error message: {response.message}'})
        except Exception as e:
            return JsonResponse({'error': str(e)})

    return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
@api_view(['POST'])
def create_robot(request):
    # print(request.body.decode('utf-8'))
    serializer = ConversationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({
            'message':'成功创建了一个机器人',
        },status = status.HTTP_200_OK)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET'])
def get_student_robots_by_id(request,student_id):
    user_robots = Conversation.objects.filter(user_id=student_id,user_type='student')
    robot_data = [
        {
            'title':conversation.title,
            'id':conversation.conversation_id,
            'role':conversation.roles,
        }
        for conversation in user_robots
    ]
    return JsonResponse({'robots':robot_data})

@csrf_exempt
@api_view(['GET'])
def get_teacher_robots_by_id(request,teacher_id):
    user_robots = Conversation.objects.filter(user_id=teacher_id,user_type='teacher')
    robot_data = [
        {
            'title':conversation.title,
            'id':conversation.conversation_id,
            'role':conversation.roles,
        }
        for conversation in user_robots
    ]
    return JsonResponse({'robots':robot_data})

@csrf_exempt
@api_view(['GET'])
def get_messages_by_robot_id(request,robot_id):
    messages = Message.objects.filter(conversation_id=robot_id)
    message_data = [
        {
            'content':message.message_content,
            'position':message.message_type,
        }
        for message in messages
    ]
    return JsonResponse({'msg':message_data},status=status.HTTP_200_OK)



