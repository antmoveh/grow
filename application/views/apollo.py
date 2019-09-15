# 测试apollo配置中心

from flask import request
from application.main.response import response_json
from config import client, namespace, node_ip, pod_namespace, pod_ip, pod_name, svc_name


# 获取apollo 参数
@response_json
def apollo_values():
    resp = {"node_ip": node_ip, "pod_name": pod_name, "pod_namespace": pod_namespace, "pod_ip": pod_ip, "svc_name": svc_name}
    request_json = request.get_json(force=True)
    for key in request_json:
        resp[key] = client.get_value(key, "default", namespace=namespace)
    return resp
