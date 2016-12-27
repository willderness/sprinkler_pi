from celery import Celery

app = Celery('tasks', broker='amqp://sprinkler:timetog3tw3t@localhost/sprinklerhost')

@app.task
def add(x, y):
    return x + y

