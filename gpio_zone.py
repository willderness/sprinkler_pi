import sys,time

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Forgot sudo")

seconds_per_unit = {"s": 1, "m": 60, "h": 3600, "d": 86400, "w": 604800}

def convert_to_seconds(s):
    return int(s[:-1]) * seconds_per_unit[s[-1]]


def run_zone(zone, time_in_seconds):
    zone_list = [11,12,13]

    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(zone_list, GPIO.OUT)
    zone = zone_list[int(sys.argv[1]) - 1] 
    
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
    print("Zone " + str(zone) + " for " + str(runtime) + " seconds.")
    run_zone(zone, runetime)

