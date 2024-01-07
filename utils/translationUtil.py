import hashlib
import time
import random

def generate_sign(q, from_lang, to_lang, appid, secret_key):
    # 生成随机码salt
    salt = str(int(time.time())) + str(random.randint(0, 10000))

    # 拼接字符串1
    sign_str = f"{appid}{q}{salt}{secret_key}"

    # 计算MD5签名
    sign_md5 = hashlib.md5(sign_str.encode()).hexdigest()

    return sign_md5, salt

def translationUtils(user_input, from_lang, to_lang, appid, secret_key):
    # 构造请求参数
    q = user_input
    sign, salt = generate_sign(q, from_lang, to_lang, appid, secret_key)

    # 构造完整请求
    request_url = f"http://api.fanyi.baidu.com/api/trans/vip/translate?q={q}&from={from_lang}&to={to_lang}&appid={appid}&salt={salt}&sign={sign}"

    return request_url

if __name__ == '__main__':
    # 用法示例
    user_input = "apple"
    from_lang = "en"
    to_lang = "zh"
    appid = "20231226001921521"
    secret_key = "qZtb4WaXNwNROlJEIFAu"
    result = translationUtils(user_input, from_lang, to_lang, appid, secret_key)
    print(result)
