import sys,time

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")


seconds_per_unit = {"s": 1, "m": 60, "h": 3600, "d": 86400, "w": 604800}

zone_list = [11,12,13]


def convert_to_seconds(s):
        return int(s[:-1]) * seconds_per_unit[s[-1]]

if len(sys.argv) < 2 or int(sys.argv[1]) > len(zone_list):
    print("bad args")
    quit() 

GPIO.setmode(GPIO.BOARD)

GPIO.setup(zone_list, GPIO.OUT)
zone = int(sys.argv[1]) - 1
runtime = convert_to_seconds(sys.argv[2])

print("Zone " + zone + " for " + runtime + " seconds.")

GPIO.output(zone,GPIO.HIGH)

time.sleep(runtime)

GPIO.output(zone,GPIO.LOW)

GPIO.cleanup()

