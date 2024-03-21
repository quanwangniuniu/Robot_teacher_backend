import json
from django.views.decorators.http import require_http_methods
from rest_framework import status
from rest_framework.decorators import api_view

from administratorhandler.serializers import MeicyModelSerializer
from conversationhandler.models import Conversation, Message
from conversationhandler.serializers import ConversationSerializer
from studenthandler.models import StudentUser
from studenthandler.serializers import StudentUserSerializer
from administratorhandler.models import AdminUser, MeicyModel
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from classroomhandler.models import RobotClassRoom
from classroomhandler.serializers import RobotClassRoomSerializer
from teacherhandler.models import TeacherUser
from teacherhandler.serializers import TeacherUserSerializer


@csrf_exempt
def adminLogin(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('inputValue_admin_username', '')
            password = data.get('inputValue_admin_pwd', '')
            admin_user = AdminUser.objects.get(username=username)
            print("AdminUser_user:",AdminUser.password)
            if password == admin_user.password:
                admin_id = admin_user.admin_id
                return JsonResponse({'message': 'Login successful','username':username,'admin_id':admin_id})
            else:
                return JsonResponse({'message': 'Login failed'}, status=401)
        except Exception as e:
            return JsonResponse({'message': 'Error during login', 'error': str(e)}, status=500)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)


@csrf_exempt
@api_view(['GET','POST'])
def getAllStudents(request):
    students = StudentUser.objects.all()
    serializer = StudentUserSerializer(students,many=True)
    return JsonResponse(serializer.data,status=status.HTTP_200_OK,safe=False)

@csrf_exempt
@api_view(['GET','POST'])
def getAllTeachers(request):
    teachers = TeacherUser.objects.all()
    serializer = TeacherUserSerializer(teachers,many=True)
    return JsonResponse(serializer.data,status=status.HTTP_200_OK,safe=False)

@csrf_exempt
@require_http_methods(["PUT"])
def edit_student_by_id(request, student_id):
    # 获取要编辑的学生对象
    student = get_object_or_404(StudentUser, student_id=student_id)
    # 从请求中获取新的学生信息
    data = json.loads(request.body)
    # 更新学生信息
    serializer = StudentUserSerializer(instance=student, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=200)
    else:
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
@require_http_methods(["POST"])
def add_student(request):
    data = json.loads(request.body)
    serializer = StudentUserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)  # 返回创建成功的学生信息，状态码为201
    else:
        return JsonResponse(serializer.errors, status=400)  # 返回错误信息，状态码为400

@csrf_exempt
@require_http_methods(["PUT"])
def edit_teacher_by_id(request, teacher_id):
    # 获取要编辑的教师对象
    teacher = get_object_or_404(TeacherUser, teacher_id=teacher_id)
    # 从请求中获取新的教师信息
    data = json.loads(request.body)
    # 更新学生信息
    serializer = TeacherUserSerializer(instance=teacher, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=200)
    else:
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
@require_http_methods(["POST"])
def add_teacher(request):
    data = json.loads(request.body)
    serializer = TeacherUserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)  # 返回创建成功的教师信息，状态码为201
    else:
        return JsonResponse(serializer.errors, status=400)  # 返回错误信息，状态码为400


@csrf_exempt
@require_http_methods(["GET"])
def getAllRobots(request):
    robots = Conversation.objects.all()
    serializer = ConversationSerializer(robots, many=True)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

@csrf_exempt
@require_http_methods(["GET"])
def getAllMessages(request):
    messages = Message.objects.all()
    serializer = ConversationSerializer(messages, many=True)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

@csrf_exempt
@require_http_methods(["GET"])
def getAllClasses(request):
    classes = RobotClassRoom.objects.all()
    serializer = RobotClassRoomSerializer(classes, many=True)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)


@csrf_exempt
@require_http_methods(["PUT"])
def edit_robot_by_id(request, conversation_id):
    # 获取要编辑的机器人对象
    robot = get_object_or_404(Conversation, conversation_id=conversation_id)
    # 从请求中获取新的对话信息
    data = json.loads(request.body)
    # 更新对话信息
    serializer = ConversationSerializer(instance=robot, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=200)
    else:
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
@require_http_methods(["PUT"])
def edit_classroom_by_id(request, class_id):
    # 获取要编辑的班级对象
    classroom = get_object_or_404(RobotClassRoom, class_id=class_id)
    # 从请求中获取新的班级信息
    data = json.loads(request.body)
    # 更新对话信息
    serializer = RobotClassRoomSerializer(instance=classroom, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=200)
    else:
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def add_class(request):
    data = json.loads(request.body)
    serializer = RobotClassRoomSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)  # 返回创建成功的班级信息，状态码为201
    else:
        return JsonResponse(serializer.errors, status=400)  # 返回错误信息，状态码为400

@csrf_exempt
@require_http_methods(["GET"])
def getAllParameters(request):
    model = MeicyModel.objects.all()
    serializer = MeicyModelSerializer(model, many=True)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

@csrf_exempt
@require_http_methods(["PUT"])
def edit_model_parameter(request):
    model = get_object_or_404(MeicyModel, model_id=1)
    data = json.loads(request.body)
    # 更新对话信息
    serializer = MeicyModelSerializer(instance=model, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=200)
    else:
        return JsonResponse(serializer.errors, status=400)