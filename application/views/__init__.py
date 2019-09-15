# 拦截请求

from application import app
from flask import request, Response
from prometheus_client import Counter, Gauge
from prometheus_client.core import CollectorRegistry
from config import svc_name

REGISTRY = CollectorRegistry(auto_describe=False)
c = Counter('requests_total', 'HTTP requests total', ['method', "IP"], registry=REGISTRY)
g = Gauge("status_code", "HTTP response code", ["method", "rule"], registry=REGISTRY)


@app.before_request
def interceptor():
	# 跳过OPTIONS请求
	if request.method == "OPTIONS":
		return
	c.labels(method=request.method, IP=svc_name).inc()


@app.after_request
def after_request(response: Response):
	g.labels(method=request.method, rule=request.url_rule).set(response.status_code)
	return response