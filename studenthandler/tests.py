from studenthandler.models import StudentUser
from django.test import TestCase
class StudentHandlerTest(TestCase):
    def test_student_create(self):
        student = StudentUser.objects.create(username='lihanwen')
        self.assertEqual(student.username,"lihanwen")
        student.save()

    def test_student_delete(self):
        student = StudentUser.objects.create(username='zongmeixi')
        zongmeixi = StudentUser.objects.get(username='zongmeixi')
        self.assertEqual(student.username,"zongmeixi")

    def test_student_getAll(self):
        students = StudentUser.objects.all()
        for student in students:
            print("student"+student)

    def test_student_login(self):
        checked_password = '123456'
        student = StudentUser.objects.get(username='liguorui')
        print(student)
        password = student.password
        print(password)
        self.assertEqual(password,checked_password)
