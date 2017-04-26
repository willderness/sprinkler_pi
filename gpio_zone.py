import sys,time

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Forgot sudo")

seconds_per_unit = {"s": 1, "m": 60, "h": 3600, "d": 86400, "w": 604800}
zone_list = [11,12,13]

def convert_to_seconds(s):
    return int(s[:-1]) * seconds_per_unit[s[-1]]


def run_zone(zone_id, time_in_seconds):

    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(zone_list, GPIO.OUT)
    zone = zone_list[int(zone_id) - 1]
    
    GPIO.output(zone,GPIO.HIGH)
    
    time.sleep(time_in_seconds)

    GPIO.output(zone,GPIO.LOW)

    GPIO.cleanup()


if __name__ == '__main__':
 
    if len(sys.argv) < 2 or int(sys.argv[1]) > len(zone_list):
        print("bad args")
        quit()


    zone = int(sys.argv[1])
    runtime = convert_to_seconds(sys.argv[2])
    descript = "Zone " + str(zone) + " for " + str(runtime) + " seconds."
    print(descript)
    run_zone(zone, runtime)

