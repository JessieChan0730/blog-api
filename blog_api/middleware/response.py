from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from blog_api.utils.result.format import render_data
from blog_api.utils.result.settings import CodeType

'''
响应消息格式化中间件
'''


class ResultMiddleware(MiddlewareMixin):
    # 白名单
    EXCLUDE_URL = ["/api/login", "/api/refresh", "/redoc/", "/swagger/", "/media/"]

    def process_response(self, request, response):
        # 如果请求的url在白名单的中，则直接返回原来的数据
        if self.is_exclude_url(request.path, self.EXCLUDE_URL):
            return response
        else:
            return self.handler_response(response)

    def is_exclude_url(self, path, urls):
        if path in urls:
            return True
        for url in urls:
            if path.startswith(url):
                return True
        return False

    def Response(self, code: int, msg=None, data=None, exps=None, headers=None):
        return JsonResponse(status=code, data=render_data(code, msg=msg, data=data, exps=exps), headers=headers)

    def handler_response(self, response):
        code = response.status_code
        if code in CodeType.SUCCESS:
            return self.Response(code=code, data=response.data)
        elif code in CodeType.ERROR or code in CodeType.NOT_CONTENT:
            return self.Response(code=code)
        elif code in CodeType.EXCEPTION:
            return self.Response(code=code, exps=response.data)
        else:
            return response
