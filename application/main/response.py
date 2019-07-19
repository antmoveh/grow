from functools import wraps
import simplejson


def response_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            resp = func(*args, **kwargs)
            return simplejson.dumps({"error-id": 0, "data": resp})
        except Exception as e:
            return simplejson.dumps({"error-id": 500, "error": str(e)})
    return wrapper
