from celery import Celery
import weather as w

app = Celery('tasks', broker='amqp://sprinkler:timetog3tw3t@localhost/sprinklerhost')

@app.task
def water_zone(zone, time_in_seconds):
    weather = w.get_current_weather()
    if w.is_clear_skies(weather):
        print("Clear to run sprinklers")
    else:
        print("Rainy day, not watering garden")

