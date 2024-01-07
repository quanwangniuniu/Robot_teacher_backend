import os
import pyqrcode
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render


def generate_qrcode(request):
    link = request.GET.get('link','')
    qr_code = pyqrcode.create(link)
    file_path = os.path.join(settings.MEDIA_ROOT,'QRCode.png')
    qr_code.png(file_path,scale=5)
    return JsonResponse({'file_path':file_path})