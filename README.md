First of all install chalice (`pip install chalice`)

To run it just run:
```bat
> chalice deploy
```
you'll see something like this:
```py
Creating Rest API
Resources deployed:
  - Lambda ARN: arn:aws:lambda:me-south-1:SOMENUMBER:function:appname-dev-func
  - Lambda ARN: arn:aws:lambda:me-south-1:SOMENUMBER:function:appname-dev
  - Rest API URL: https://VALUE.execute-api.me-south-1.amazonaws.com/api/
```
then just
```bat
> curl -X GET https://VALUE.execute-api.me-south-1.amazonaws.com/api/
```
to get response from the lambda
