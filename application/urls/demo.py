
from application import app
from application.views import demo
from application.views import apollo


# 测试模拟接口
app.add_url_rule("/demo/random/sleep", view_func=demo.random_sleep, methods=["GET"])
app.add_url_rule("/demo/server/info", view_func=demo.server_info, methods=["GET"])
app.add_url_rule("/demo/error/code", view_func=demo.error_code, methods=["GET"])
app.add_url_rule("/demo/error/net", view_func=demo.error_net, methods=["GET"])

# apollo 测试
app.add_url_rule("/demo/apollo/values", view_func=apollo.apollo_values, methods=["POST"])