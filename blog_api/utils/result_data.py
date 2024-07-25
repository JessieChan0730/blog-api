class ResultData:
    @staticmethod
    def generate_response(code: int, msg: str, data):
        return {
            'code': code,
            'msg': msg,
            'data': data
        }

    @staticmethod
    def ok_200(data: object, msg='请求成功'):
        return ResultData.generate_response(200, msg, data)

    @staticmethod
    def unauthorized_401(msg='暂无权限'):
        return ResultData.generate_response(401, msg, {})

    @staticmethod
    def bad_request_400(msg='无效请求'):
        return ResultData.generate_response(400, msg, {})

    @staticmethod
    def not_found_404(msg='暂时未找到资源'):
        return ResultData.generate_response(404, msg, {})
