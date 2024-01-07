import requests
from django.test import TestCase
from utils import translationUtil,extractTranslationApiUtil


# Create your tests here.
def translationTest():
    text_to_translate = '这个是测试，祝你全家身体健康！'
    # API密钥
    secret_key = 'qZtb4WaXNwNROlJEIFAu'
    appid = "20231226001921521"
    baidu_api_url = translationUtil.translationUtils(text_to_translate, "zh", "en", appid, secret_key)
    response = requests.get(baidu_api_url)
    translation_result = response.json()
    print(translation_result)
    final_result = extractTranslationApiUtil.extract_translation(translation_result)
    print("final:",final_result)


if __name__ == '__main__':
    translationTest()