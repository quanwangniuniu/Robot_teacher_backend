'''
  发送邮件服务需要先在settings服务里面配置邮箱信息，本项目由于未进行商用因此暂未设置邮箱地址发送邮件

    #settings.py
    EMAIL_BACKEND = 'djanggo.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.example.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'your_username@example.com'
    EMAIL_HOST_PASSWORD = 'your_password'
    EMAIL_USE_TLS = True
'''


from django.core import mail
from django.core.mail import BadHeaderError,send_mail
from django.http import HttpResponse,HttpResponseRedirect

# send-email test
def send_email(request):
    subject = request.POST.get('subject','')
    message = request.POST.get('message','')
    from_email = request.POST.get('from_email','')
    if subject and message and from_email:
        try:
            send_mail(subject,message,from_email,['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/test/contact')
    else:
        return HttpResponse('make sure all fields are entered and valid.')

# multiple sending
def moltiple_sending_test():
    connection = mail.get_connection()
    connection.open()
    # Construct an email message that uses the connection
    email1 = mail.EmailMessage(
        'Hello',
        'Body goes here',
        'from@example.com',
        ['to1@example.com'],
        connection = connection
    )
    email1.send() # send the email

    # Construct two more messages
    email2 = mail.EmailMessage(
        'Hi, email test 2',
        'Body2 goes here',
        'from@example.com',
        ['to2@example.com'],
    )

    email3 = mail.EmailMessage(
        'Hi, email test 3',
        'Body3 goes here',
        'from@example.com',
        ['to3@example.com'],
    )
    # send the two emails in a single call
    connection.send_messages([email2,email3])
    # manually close the connection
    connection.close()

if __name__ == '__main__':
    moltiple_sending_test()
