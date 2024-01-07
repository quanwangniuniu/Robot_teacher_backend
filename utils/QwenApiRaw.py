import dashscope

dashscope.api_key = "sk-ed6d4a77b7b343679f7860466e562247"

# 实现基本的自然语言调用模型

def sample_sync_call_streaming():
    prompt_text = '写一个递归程序,斐波那契数列，写一个c++代码'
    response_generator = dashscope.Generation.call(
        model='qwen-max',
        prompt=prompt_text,
        stream=True,
        top_p=0.8)

    head_idx = 0
    for resp in response_generator:
        paragraph = resp.output['text']
        print("\r%s" % paragraph[head_idx:len(paragraph)], end='')
        if(paragraph.rfind('\n') != -1):
            head_idx = paragraph.rfind('\n') + 1




if __name__ == '__main__':
    # call_with_messages()
    sample_sync_call_streaming()