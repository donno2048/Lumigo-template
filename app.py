import json
app = __import__('lumigo_tracer').LumigoChalice(__import__('chalice').Chalice(app_name = "appname"), token = YOUR_LUMIGO_KEY)
@app.lambda_function()
def func(event, context):return{'statusCode':200,'body':json.dumps('Hi!')}
@app.route("/")
def index(): return {'statusCode':200,'body':json.dumps('Hello!')}
