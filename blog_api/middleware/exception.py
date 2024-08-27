from django.utils.deprecation import MiddlewareMixin
from rest_framework.views import exception_handler

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
    # TODO 发送邮件
    print(f"抓到你了：{str(exc)}")
    return exception_handler(exc, context)
