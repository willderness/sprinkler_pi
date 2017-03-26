import gpio_zone, pushjet
import tasks
import sys

#service_resp = pushjet.register_service("Sprinkler", "http://digibyte.com/waterdrop.png")
#service_secret = service_resp['secret']
#service_public = service_resp['public']


if __name__ == '__main__':
 
    if len(sys.argv) < 2 or int(sys.argv[1]) > len(zone_list):
        print("bad args")
        quit()
    
    zone = int(sys.argv[1])
    runtime = gpio_zone.convert_to_seconds(sys.argv[2])
    tasks.water_zone(zone, runetime)



