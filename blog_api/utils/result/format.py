from .settings import CODE_MSG_MAP

'''
成功消息格式：
{
    "code": 2xx,
    "msg": "请求成功",
    "data": []
}
请求异常消息格式：
{
    "code": 400,
    "msg": "请求存在问题",
    "exps": []
}
服务器异常
{
    "code": 500,
    "msg": "服务器异常，请稍后重试",
}
'''


def render_data(code: int, msg=None, data=None, exps=None):
    response_data = {
        "code": code,
    }
    if msg is not None:
        response_data["msg"] = msg
    else:
        response_data["msg"] = get_msg_by_code(code)
    if data is not None:
        response_data["data"] = data
    if exps is not None:
        response_data["exps"] = exps
    return response_data


def get_msg_by_code(code: int):
    return CODE_MSG_MAP.get(code, "响应消息类型未知")
