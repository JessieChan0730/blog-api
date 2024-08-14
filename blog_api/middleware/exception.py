from django.utils.deprecation import MiddlewareMixin

'''
异常捕获中间件
'''


class ExceptionHandlerMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        # TODO 发送邮件
        print(f"抓到你了：{str(exception)}")
        # 直接转让到其他中间件
        return None
