from rest_framework.views import exception_handler

def custom_exception_handler(exc,context):
    response = exception_handler(exc,context)
    if response is not None:
        data = response.data
        response.data = {}
        for field,value in data.items():
            if isinstance(value, list):
                value = value[0]
            if isinstance(value, dict):
                for k,v in value.items():
                    response.data[k] = v[0].title()
            response.data[field] = value
    return response
