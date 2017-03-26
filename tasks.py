from celery import Celery
import weather as w
import gpio_zone
import pushjet

service_public = "98ea-852f0b-fae6206b53db-76fbe-43d1a982c"
service_secret = "a65e46e7af577920572503dbcd332c43"


app = Celery('tasks', broker='amqp://sprinkler:timetog3tw3t@localhost/sprinklerhost')

@app.task
def water_zone(zone, time_in_seconds):
    weather = w.get_current_weather()
    if w.is_clear_skies(weather):
        print("Clear to run sprinklers")
        descript = "Zone " + str(zone) + " for " + str(runtime) + " seconds."
        pushjet.push_msg(service_secret, descript)
        gpio_zone.run_zone(zone, time_in_seconds);
    else:
        msg = "Rainy day, not watering garden"
        print(msg)
        pushjet.push_msg(service_secret, msg)

