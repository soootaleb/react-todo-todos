import json

def main_view(request, format = None):
    body = json.dumps(request.data)
    print(body)
    return True