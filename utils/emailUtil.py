from django.core.mail import EmailMessage

email = EmailMessage(
    subject="邮件标题",
    body="邮件主体",
    from_email="hunterxxx@163.com",
    to=["120460xxx@qq.com"],
)
email.send()


