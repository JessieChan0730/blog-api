import threading

from django.conf import settings
from django.core.mail import send_mail


def send_email(target: str, title: str, message: str, html_message: str = ''):
    t = threading.Thread(
        target=send_mail,
        args=(
            title,  # 邮件标题
            message,  # 邮件内容（文本），有html_message参数，这里配置失效
            settings.EMAIL_HOST_USER,  # 用于发送邮件的邮箱地址，配置授权码的邮箱
            [target],  # 接收邮件的邮件地址，可以写多个
        ),
        # html_message中定义的字符串即HTML格式的信息，可以在一个html文件中写好复制出来放在该字符串中
        kwargs={
            'html_message': html_message
        })
    t.start()
