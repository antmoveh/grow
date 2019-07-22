import requests
from config import logger
import time

demo_random_sleep = "/demo/random/sleep"
demo_server_info = "/demo/server/info"
demo_error_code = "/demo/error/code"
server_ip = "http://127.0.0.1:8008"
protect_pod_name = "non"  # 被保护的pod，接收到此值时会跳过错误逻辑
headers = {
    'Host': "server-dispatch.server",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0"
}

# 网络错误
def NetworkErrorRatio():
    with requests.Session() as s:
        s.headers.update(headers)
        for i in range(100):
            x1 = s.get(url=server_ip + demo_random_sleep)
            logger.info(x1.status_code)
            logger.info(x1.text)


# 延迟大约500 ms
def LatencyAtQuantileMS():
    with requests.Session() as s:
        s.headers.update(headers)
        for i in range(100):
            time.sleep(1)
            url = server_ip+demo_random_sleep
            x1 = s.get(url=url)
            logger.info(x1.text)


# 响应错误率
def ResponseCodeRatio():
    with requests.Session() as s:
        s.headers.update(headers)
        for i in range(100):
            x1 = s.get(url=server_ip+demo_error_code)
            print(x1.url)
            logger.info(x1.status_code)
            logger.info(x1.text)


if __name__ == "__main__":
    server_ip = "http://39.106.1.207/v1"
    # NetworkErrorRatio()
    LatencyAtQuantileMS()
    # ResponseCodeRatio()