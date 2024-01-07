import random
from http import HTTPStatus
from dashscope import Generation
import dashscope
from dashscope.api_entities.dashscope_response import Role
dashscope.api_key = "sk-ed6d4a77b7b343679f7860466e562247"

def multi_round_conversation():
    messages = [{'role': Role.SYSTEM, 'content': '你是一个代码工程师.'}]

    while True:
        user_input = input('User: ')
        if user_input == '-1':
            break

        messages.append({'role': Role.USER, 'content': user_input})

        response = Generation.call(
            'qwen-max',
            messages=messages,
            seed=random.randint(1, 10000),
            result_format='message',
        )

        if response.status_code == HTTPStatus.OK:
            print("Robot:", end=' ')
            print(response.output.choices[0]['message']['content'])
            messages.append({'role': response.output.choices[0]['message']['role'],
                             'content': response.output.choices[0]['message']['content']})
        else:
            print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
                response.request_id, response.status_code,
                response.code, response.message
            ))

if __name__ == '__main__':
    multi_round_conversation()