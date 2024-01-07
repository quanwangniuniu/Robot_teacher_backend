'''
 一个自动的二维码生成工具
'''
import os
import pyqrcode
from PIL import Image
from django.conf import settings
from django.http import JsonResponse


def QRcodeGenerate(input):
    link = input("在这里输入链接来生成二维码: ")
    qr_code = pyqrcode.create(link)
    file_path = os.path.join(settings.MEDIA_ROOT, 'QRCode.png')
    qr_code.png(file_path, scale=5)
    return JsonResponse({'file_path': file_path})