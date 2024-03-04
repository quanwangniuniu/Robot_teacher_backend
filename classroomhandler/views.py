from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from teacherhandler.models import TeacherUser
from .models import RobotClassRoom
from .serializers import RobotClassRoomSerializer
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