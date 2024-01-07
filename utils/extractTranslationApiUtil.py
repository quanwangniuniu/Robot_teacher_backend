def extract_translation(json_data):
    try:
        # 尝试获取 'trans_result' 中的第一个元素的 'dst' 值
        translation = json_data['trans_result'][0]['dst']
        return translation
    except (KeyError, IndexError):
        # 处理可能的键错误或索引错误
        print("Error: Unable to extract translation from JSON data.")
        return None

# 用法示例
if __name__ == '__main__':
    json_data = {'from': 'zh', 'to': 'en', 'trans_result': [{'src': '这个是测试，祝你全家身体健康！', 'dst': 'This is a test. Wishing you and your whole family good health!'}]}
    translation_result = extract_translation(json_data)
    if translation_result:
        print("提取的翻译结果:", translation_result)
    else:
        print("无法提取翻译结果.")