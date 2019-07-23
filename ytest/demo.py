from config import logger
import time
import http.client
import simplejson

# https://www.jianshu.com/p/32cd4b9d5a04
# 原来我也以为requests 无所不能 血泪教训啊

demo_random_sleep = "/v1/demo/random/sleep"
demo_server_info = "/v1/demo/server/info"
demo_error_code = "/v1/demo/error/code"
demo_error_net = "/v1/demo/error/net"
server_ip = "http://127.0.0.1:8008"
protect_pod_name = "?protect_pod_name=demo-xswtk"  # 被保护的pod，接收到此值时会跳过错误逻辑
host = "server-dispatch.server"


# 网络错误
def NetworkErrorRatio():
    try:
        params = simplejson.dumps({})
        headers = {"Content-type": "text/json", "Accept": "text/plain", "Host": "server-dispatch.server"}
        conn = http.client.HTTPConnection(server_ip)
        url = demo_server_info
        conn.request('GET', url=url, body=params, headers=headers)
        response = conn.getresponse()
        logger.info(response.status)
        logger.info(response.read().decode('utf-8'))
        conn.close()
    except Exception as e:
        logger.error(e)


# 延迟大于500ms
def LatencyAtQuantileMS():
    try:
        params = simplejson.dumps({})
        headers = {"Content-type": "text/json", "Accept": "text/plain", "Host": "server-dispatch.server"}
        url = demo_random_sleep + protect_pod_name
        conn = http.client.HTTPConnection(server_ip)
        conn.request('GET', url=url, body=params, headers=headers)
        response = conn.getresponse()
        logger.info(response.status)
        logger.info(response.read().decode('utf-8'))
        conn.close()
    except Exception as e:
        logger.error(e)


# 响应错误率
def ResponseCodeRatio():
    try:
        params = simplejson.dumps({})
        headers = {"Content-type": "text/json", "Accept": "text/plain", "Host": "server-dispatch.server"}
        url = demo_error_code + protect_pod_name
        conn = http.client.HTTPConnection(server_ip)
        conn.request('GET', url=url, body=params, headers=headers)
        response = conn.getresponse()
        logger.info(response.status)
        logger.info(response.read().decode('utf-8'))
        conn.close()
    except Exception as e:
        logger.error(e)


# 延迟大于500ms
def LatencyAndResponse():
    try:
        params = simplejson.dumps({})
        headers = {"Content-type": "text/json", "Accept": "text/plain", "Host": "server-dispatch.server"}
        url = demo_error_net + protect_pod_name
        conn = http.client.HTTPConnection(server_ip)
        conn.request('GET', url=url, body=params, headers=headers)
        response = conn.getresponse()
        logger.info(response.status)
        logger.info(response.read().decode('utf-8'))
        conn.close()
    except Exception as e:
        logger.error(e)


def recycle_call(func):
    for i in range(1000):
        time.sleep(0.5)
        logger.info(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        func()


if __name__ == "__main__":
    server_ip = "39.106.1.207"
    # server_ip = "10.203.40.97"
    # NetworkErrorRatio()
    # LatencyAtQuantileMS()
    # ResponseCodeRatio()
    recycle_call(ResponseCodeRatio)