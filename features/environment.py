def before_scenario(context, scenario):
    context.base_url = "http://127.0.0.1:8000/api/v2"
    context.headers = {'Content-Type': 'application/json'}

def after_scenario(context, scenario):
    pass