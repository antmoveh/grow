
from application import app
from application.views import demo


# 测试模拟接口
app.add_url_rule("/demo/random/dispose", view_func=demo.random_dispose, methods=["GET"])
app.add_url_rule("/demo/node/info", view_func=demo.node_info, methods=["GET"])
app.add_url_rule("/demo/error", view_func=demo.error, methods=["GET"])