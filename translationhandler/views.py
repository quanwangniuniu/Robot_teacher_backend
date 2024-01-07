from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt

from utils import translationUtil
from utils import extractTranslationApiUtil
# 翻译模块

@csrf_exempt
def text_translation(request):
    if request.method == 'GET':
        # 获取前端传递的翻译内容参数
        text_to_translate = request.GET.get('text_to_translate', '')
        from_lang = request.GET.get('from_lang')
        to_lang = request.GET.get('to_lang')
        if not text_to_translate:
            return JsonResponse({'error': 'Please provide text to translate.'}, status=400)

        # API密钥
        secret_key = 'qZtb4WaXNwNROlJEIFAu'
        appid = "20231226001921521"
        baidu_api_url = translationUtil.translationUtils(text_to_translate,from_lang,to_lang,appid,secret_key)
        response = requests.get(baidu_api_url)
        translation_result = response.json()
        final_result = extractTranslationApiUtil.extract_translation(translation_result)
        # 处理翻译结果
        return JsonResponse({'translation_result': final_result},status=200)


    else:
        return JsonResponse({'error': 'Invalid request method. Use GET.'}, status=405)
