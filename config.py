import os
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')
logger = logging.getLogger()


node_ip = os.getenv("NODE_NAME", "default")
pod_name = os.getenv("POD_NAME", "default")
pod_namespace = os.getenv("POD_NAMESPACE", "default")
pod_ip = os.getenv("POD_IP", "default")


pod_info = {"node_ip": node_ip, "pod_name": pod_name, "pod_namespace": pod_namespace, "pod_ip": pod_ip}