from lumigo_tracer import LumigoChalice
from chalice import Chalice
import json
app = Chalice(app_name = "appname")
app = LumigoChalice(app, token = YOUR_LUMIGO_KEY)
@app.lambda_function()
def func(event, context):return{'statusCode':200,'body':json.dumps('Hi!')}
@app.route("/")
def index(): return {'statusCode':200,'body':json.dumps('Hello!')}
