
from . import *
from config import client, namespace, node_ip, pod_namespace, pod_ip, pod_name


# 获取apollo 参数
@response_json
def apollo_values():
    resp = {"node_ip": node_ip, "pod_name": pod_name, "pod_namespace": pod_namespace, "pod_ip": pod_ip}
    request_json = request.get_json(force=True)
    for key in request_json:
        resp[key] = client.get_value(key, "default", namespace=namespace)
    return resp
