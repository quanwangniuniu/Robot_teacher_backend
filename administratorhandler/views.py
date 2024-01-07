import json
from administratorhandler.models import AdminUser
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
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