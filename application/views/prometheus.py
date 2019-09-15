# prometheus exporter

import prometheus_client
from flask import Response
from . import REGISTRY


def metrics():
	return Response(prometheus_client.generate_latest(REGISTRY), mimetype="text/plain")