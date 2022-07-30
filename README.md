# fastapi-board


## Dependencies

## How to use

```
$ source ./venv/bin/activate
```
```
$ pip3 install -r requirements
```
```
$ gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8080 --reload
```

