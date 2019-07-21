import requests
from config import logger

demo_random_sleep = "/demo/random/sleep"
demo_server_info = "/demo/server/info"
demo_error = "/demo/error/code"
server_ip = "http://127.0.0.1:8008"
protect_pod_name = "non"  # 被保护的pod，接收到此值时会跳过错误逻辑
header = {"Host": "server-dispatch.server"}


# 网络错误
def NetworkErrorRatio():
    for i in range(10):
        x1 = requests.get(url=server_ip + demo_random_sleep)
        logger.info(x1.status_code)
        logger.info(x1.text)


# 延迟大约500 ms
def LatencyAtQuantileMS():
    for i in range(10):
        x1 = requests.get(url=server_ip+demo_random_sleep)
        logger.info(x1.status_code)
        logger.info(x1.text)


# 响应错误率
def ResponseCodeRatio():
    for i in range(10):
        x1 = requests.get(url=server_ip+demo_error)
        logger.info(x1.status_code)
        logger.info(x1.text)


if __name__ == "__main__":
    server_ip = "http://127.0.0.1:8008"
    # NetworkErrorRatio()
    # LatencyAtQuantileMS()
    ResponseCodeRatio()