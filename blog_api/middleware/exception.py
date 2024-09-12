from django.utils.deprecation import MiddlewareMixin
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework_simplejwt.exceptions import AuthenticationFailed, InvalidToken

'''
异常捕获中间件
用于捕获代码中逻辑异常
'''


class ExceptionHandlerMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        # TODO 发送邮件
        print(f"抓到你了：{str(exception)}")
        # 直接转让到其他中间件
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

    # TODO 发送邮件
    print(f"抓到你了：{str(exc)}")
    return exception_handler(exc, context)
