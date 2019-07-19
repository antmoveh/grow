from . import *
from config import node_ip


# sleep random time
@response_json
def random_dispose():
    pass


# 节点信息
@response_json
def node_info():

    return node_ip


# return error code
@response_json
def error():
    return