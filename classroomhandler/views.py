from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from studenthandler.models import StudentUser
from teacherhandler.models import TeacherUser
from .models import RobotClassRoom, ClassRoomMessage
from .serializers import RobotClassRoomSerializer
from conversationhandler.models import Message
from aip import AipNlp

APP_ID = '55095226'
API_KEY = 'illTXbudO1jWmuXAad1NEPyo'
SECRET_KEY = '6EogFbwnmNYH30H9MQpfIcUYZNbYtPWs'

client = AipNlp(APP_ID,API_KEY,SECRET_KEY)
@csrf_exempt
@api_view(['POST'])
def create_class(request):
    if request.method == 'POST':
       # 从Post请求中获取数据:
       class_name = request.POST.get('class_name')
       teacher_id = request.POST.get('teacher_id')
       # 获取老师对象
       teacher = TeacherUser.objects.get(teacher_id = teacher_id)

       # 创建班级对象
       classroom = RobotClassRoom(class_name=class_name)
       classroom.save()

       # 添加老师到班级中
       classroom.teacher.add(teacher)
       # 使用序列化器将班级对象序列化为JSON格式
       serializer = RobotClassRoomSerializer(classroom)
       return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
    else:
       return JsonResponse({'error': 'Only POST requests are allowed'}, status=400)

# 老师加入班级
@csrf_exempt
@api_view(['POST'])
def teacher_participate_class(request):
    if request.method == 'POST':
        teacher_id = request.POST.get('teacher_id')
        class_name = request.POST.get('class_name')
        # 根据班级名称获取班级对象
        classroom = RobotClassRoom.objects.get(class_name=class_name)
        # 获取老师对象
        teacher = TeacherUser.objects.get(teacher_id = teacher_id)
        classroom.teacher.add(teacher)
        # 序列化
        serializer = RobotClassRoomSerializer(classroom)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=400)


# 学生加入班级
@csrf_exempt
@api_view(['POST'])
def student_participate_class(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        class_name = request.POST.get('class_name')
        # 根据班级名称获取班级对象
        classroom = RobotClassRoom.objects.get(class_name=class_name)
        # 获取学生对象
        student = StudentUser.objects.get(student_id = student_id)
        classroom.student.add(student)
        # 序列化
        serializer = RobotClassRoomSerializer(classroom)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=400)

@csrf_exempt
@api_view(['PUT'])
def edit_class(request, class_id):
    try:
        cls = RobotClassRoom.objects.get(class_id=class_id)
    except RobotClassRoom.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = RobotClassRoomSerializer(cls, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET'])
def get_teacher_classrooms(request, teacher_id):
    try:
        teacher = TeacherUser.objects.get(teacher_id=teacher_id)
        classrooms = teacher.classrooms.all()
        # 构造班级信息的字典列表
        classrooms_info = []
        for classroom in classrooms:
            classrooms_info.append({
                'class_id': classroom.class_id,
                'class_name': classroom.class_name,
                'class_avatar': classroom.class_avatar,
                # 添加其他需要的字段
            })

        # 返回JSON响应
        return JsonResponse({'classrooms': classrooms_info})

    except TeacherUser.DoesNotExist:
        return JsonResponse({'error': 'Teacher not found'}, status=404)


@csrf_exempt
@api_view(['GET'])
def get_student_classrooms(request, student_id):
    try:
        student = StudentUser.objects.get(student_id=student_id)
        classrooms = student.classrooms.all()
        # 构造班级信息的字典列表
        classrooms_info = []
        for classroom in classrooms:
            classrooms_info.append({
                'class_id': classroom.class_id,
                'class_name': classroom.class_name,
                'class_avatar': classroom.class_avatar,
                # 添加其他需要的字段
            })
        # 返回JSON响应
        return JsonResponse({'classrooms': classrooms_info})

    except StudentUser.DoesNotExist:
        return JsonResponse({'error': 'Student not found'}, status=404)


@csrf_exempt
@api_view(['GET'])
def get_users_in_classrooms(request, class_id):
    try:
        classroom = RobotClassRoom.objects.get(class_id=class_id)
        # 获取与该班级编号关联的所有教师和学生
        teachers = classroom.teacher.all()
        students = classroom.student.all()
        # 构造用户信息的字典列表
        users_info = []
        for teacher_user in teachers:
            users_info.append({
                'user_name': teacher_user.username,
                'user_email': teacher_user.email,
                'avatar':teacher_user.teacher_avatar,
            })

        for student_user in students:
            users_info.append({
                'user_name': student_user.username,
                'user_email': student_user.email,
                'avatar':student_user.student_avatar,
            })

        # 返回JSON响应
        return JsonResponse({'users_info': users_info},status=status.HTTP_200_OK)

    except RobotClassRoom.DoesNotExist:
        return JsonResponse({'error': 'ClassRooms not found'}, status=404)


@csrf_exempt
@api_view(['GET'])
def get_classroom_name_byId(request,class_id):
    classroom = RobotClassRoom.objects.get(class_id=class_id)
    return JsonResponse(classroom.class_name,status=200,safe=False)

@csrf_exempt
@api_view(['GET'])
def get_classroom_messages(request,class_id):
    try:
        classroom_messages = ClassRoomMessage.objects.filter(class_id=class_id)
        classroom_info = []
        for message in classroom_messages:
            info = {
                'message_id': message.message_id,
                'class_id':message.class_id,
                'message_content':message.message_content,
                'user_name':message.user_name,
                'user_type':message.user_type,
                'message_avatar':message.message_avatar
            }
            classroom_info.append(info)
        # 返回包含当前班级所有信息的 JSON 响应
        return JsonResponse({'classroom_info':classroom_info})
    except ClassRoomMessage.DoesNotExist:
        return JsonResponse({'classroom_info':[]})

@csrf_exempt
@api_view(['POST'])
def sendMessage(request,class_id,username):
    data = request.body.decode('utf-8')
    message = ClassRoomMessage()
    message.class_id = class_id
    message.user_name = username
    def check_user_role(username):
        is_student = StudentUser.objects.filter(username=username).exists()
        is_teacher = TeacherUser.objects.filter(username=username).exists()
        if is_student and not is_teacher:
            return "student"
        elif is_teacher and not is_student:
            return "teacher"
        else:
            return "unknown"
    message.user_type = check_user_role(username)
    if check_user_role(username)=='student':
        message.message_avatar = StudentUser.objects.get(username=username).student_avatar
    else:
        message.message_avatar = TeacherUser.objects.get(username=username).teacher_avatar
    message.message_content = data
    message.save()
    return JsonResponse("success send message",status=status.HTTP_200_OK,safe=False)

# 关键词和数据分析提取
@csrf_exempt
@api_view(['GET'])
def substract_tags(request):
    # 获取所有Message实例
    all_messages = Message.objects.filter(message_type='right')

    # 使用列表推导式提取message_content字段的值
    message_contents_list = [message.message_content for message in all_messages]
    # # 打印列表长度
    # print("Length of message_contents_list:", len(message_contents_list))


    # for content in message_contents_list:
    #     result = client.keyword('软件工程', content)
    #     print("result:-------")
    #     print(result)
    #     print(content)

        # 将列表转换为JSON响应格式
    response_data = {
        'message_contents': message_contents_list
    }

    # 返回JSON响应
    return JsonResponse(response_data)

@csrf_exempt
@api_view(['GET'])
def get_teacher_avatar(request,teacher_id):
    return JsonResponse(TeacherUser.objects.get(teacher_id=teacher_id).teacher_avatar,status=200,safe=False)

@csrf_exempt
@api_view(['GET'])
def get_student_avatar(request,student_id):
    return JsonResponse(StudentUser.objects.get(student_id=student_id).student_avatar,status=200,safe=False)