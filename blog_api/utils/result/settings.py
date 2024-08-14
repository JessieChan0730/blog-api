# 状态码和消息映射
CODE_MSG_MAP = {
    200: "请求成功",
    201: "创建成功",
    204: "删除成功",
    404: "请求的资源不存在",
    405: "请求方法不被允许",
    401: "暂无权限",
    400: "请求参数错误",
    500: "服务器内部错误，请稍等"
}


# code 代码含义
class CodeType:
    NOT_CONTENT = [204]
    SUCCESS = [200, 201]
    EXCEPTION = [400]
    ERROR = [404, 401, 500, 405]
