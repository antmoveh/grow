from . import *
from config import pod_info, pod_name
from flask import Response
import random
import simplejson
import time


# sleep random time
@response_json
def random_sleep():
    pod_info["type"] = "random_sleep"
    # 传入被保护的pod的name,可正常返回
    protect_pod_name: str = request.values.get("protect_pod_name", "pod")
    if pod_name.startswith(protect_pod_name):
        pod_info["protect"] = True
        pod_info["wait"] = "waiting 0 ms"
        return pod_info
    t = random.randint(1, 100)
    time.sleep(t/100)
    pod_info["wait"] = "waiting %d0 ms" % t
    return pod_info


# return pod info
@response_json
def server_info():
    return pod_info


# return error code
def error_code():
    pod_info["type"] = "error_code"
    # 传入被保护的pod的name,可正常返回
    protect_pod_name: str = request.values.get("protect_pod_name", "pod")
    if pod_name.startswith(protect_pod_name):
        pod_info["protect"] = True
        return simplejson.dumps({"error-id": 0, "data": pod_info})
    # 按比率随机返回错误状态
    if random.randint(1, 100) > 50:
        return Response(simplejson.dumps({"error-id": 500, "data": pod_info}), status=500, mimetype='application/json')

    return simplejson.dumps({"error-id": 0, "data": pod_info})


# return error net
def error_net():
    pod_info["type"] = "error_net"
    # 传入被保护的pod的name,可正常返回
    protect_pod_name: str = request.values.get("protect_pod_name", "pod")
    if pod_name.startswith(protect_pod_name):
        pod_info["protect"] = True
        return simplejson.dumps({"error-id": 0, "data": pod_info})
    # 按比率随机返回错误状态
    if random.randint(1, 100) > 50:
        time.sleep(180)
        return Response(simplejson.dumps({"error-id": 500, "data": pod_info}), status=500, mimetype='application/json')

    return simplejson.dumps({"error-id": 0, "data": pod_info})