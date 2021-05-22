web: gunicorn WhiteCow.wsgi --log-file -
beat: celery -A WhiteCow  beat -l INFO
worker: celery -A WhiteCow  worker -l INFO