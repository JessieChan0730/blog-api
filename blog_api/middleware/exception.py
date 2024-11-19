import traceback

from django.conf import settings
from django.contrib.auth.models import User
from django.utils.deprecation import MiddlewareMixin
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework_simplejwt.exceptions import AuthenticationFailed, InvalidToken

from blog_api.utils.email import send_html_email

'''
异常捕获中间件
用于捕获代码中逻辑异常
'''


class ExceptionHandlerMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        # 只有一个用户，直接获取
        user = User.objects.first()
        print(f"抓到你了：{str(exception)}")
        if not settings.DEBUG:
            send_html_email(target=user.email, subject="后端服务异常", template="email/exception_email_template.html",
                            context={
                                "error": traceback.format_exc()
                            })
        return None


'''
异常捕获函数
用于捕获drf中，接口中的产生的异常
'''


def custom_exception_handler(exc, context):
    # 调用 DRF 的默认异常处理函数
    if isinstance(exc, InvalidToken):
        return Response(data={
            'detail': "登录信息过期，请重新登录"
        }, status=status.HTTP_401_UNAUTHORIZED)
    # 自定义异常返回信息
    if isinstance(exc, AuthenticationFailed):
        return Response(data={
            'detail': str(exc)
        }, status=status.HTTP_401_UNAUTHORIZED)
    return exception_handler(exc, context)
