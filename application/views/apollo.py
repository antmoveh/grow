
from . import *
from config import client, namespace


# 获取apollo 参数
@response_json
def apollo_values():
    resp = dict()
    request_json = request.get_json(force=True)
    for key in request_json:
        resp[key] = client.get_value(key, "default", namespace=namespace)
    return resp
