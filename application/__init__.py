"""
flask app 初始化，连接db/jenkins等操作在需要时候连接
"""
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources=r'/*')
# app.config.from_pyfile("config.py")
app.secret_key = 'F12Zr47j\3yX R~X@H!jLwf/T'
app.debug = True


# 注册路由文件
from .urls import *
from .views import *