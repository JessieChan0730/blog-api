import threading

from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
'''
发送文本邮件
Args:
    target: 目标邮箱地址
    title: 邮箱主题
    message: 文本信息
    html_message: HTML信息

Returns:
    None
'''


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


'''
发送html邮件
Args:
    target: 目标邮箱地址
    subject: 邮箱主题
    template: 模板路径
    context: 模板上下文
    
Returns:
    None
'''


def send_html_email(target: str, subject: str, template: str, context: dict):
    context["email_image_url"] = settings.EMAIL_IMAGE_URL
    context["email_callback_url"] = settings.EMAIL_CALLBACK_URL
    html_content = render_to_string(template, context)
    email = EmailMessage(
        subject,
        body='',
        from_email=settings.EMAIL_HOST_USER,
        to=[target],
        headers={'Content-Type': 'text/html', 'Reply-To': settings.EMAIL_HOST_USER},
    )
    email.content_subtype = 'html'  # 设置邮件内容为 HTML
    email.body = html_content
    t = threading.Thread(target=email.send)
    t.start()
