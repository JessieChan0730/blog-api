from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

from .result_data import ResultData

'''
统一数据返回中间件
数据返回格式为：
    {
        "code":200,
        "data":[],
        "msg":"请求成功"
    }
'''


class ResultMiddleware(MiddlewareMixin):
    # 白名单
    EXCLUDE_URL = ["/api/login", "/api/refresh"]

    def process_response(self, request, response):
        # 如果请求的url在白名单的中，则直接返回原来的数据
        if request.path in self.EXCLUDE_URL:
            return response

        if response.status_code == 200:
            return JsonResponse(status=response.status_code, data=ResultData.ok_200(response.data))
        elif response.status_code == 404:
            return JsonResponse(status=response.status_code, data=ResultData.not_found_404())
        elif response.status_code == 401:
            return JsonResponse(status=response.status_code, data=ResultData.unauthorized_401())
        elif response.status_code == 400:
            return JsonResponse(status=response.status_code, data=ResultData.bad_request_400())
        elif response.status_code == 500:
            return JsonResponse(status=response.status_code, data=ResultData.server_bad_500())
        return response
