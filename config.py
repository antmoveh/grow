import os
import logging
import threading
from pyapollo import ApolloClient

logging.basicConfig(level=logging.INFO,
                    filename="new.log",
                    filemode="a",
                    format='%(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')
logger = logging.getLogger()

node_ip = os.getenv("NODE_NAME", "default")
pod_name = os.getenv("POD_NAME", "default")
pod_namespace = os.getenv("POD_NAMESPACE", "default")
pod_ip = os.getenv("POD_IP", "default")


app_id = os.getenv("APP_ID", "SampleApp")
cluster = os.getenv("CLUSTER", "default")
config_server_url = os.getenv("CONFIG_SERVER_URL", "http://localhost:8080")
svc_name = os.getenv("SVC_NAME")
namespace = os.getenv("NAMESPACE", "default")


client = ApolloClient(app_id=app_id, cluster=cluster, config_server_url=config_server_url, timeout=65, ip=svc_name)
#client.start()
t = threading.Thread(target=client.start, kwargs={"catch_signals": False})
t.start()