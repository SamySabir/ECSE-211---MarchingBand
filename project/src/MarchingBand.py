import threading
import time
import EmergencyStopDesign
import speaker_button 
from drum_class_and_test import drummer
from utils.brick import EV3UltrasonicSensor, wait_ready_sensors, reset_brick, BP


event = threading.Event()
activated = False
flute_start = threading.Thread(target=speaker_button.flute, args=(event, activated))
drumming = threading.Thread(target=drummer, args=(event, activated))
#emergency_stop = threading.Thread(target=EmergencyStopDesign.emergency_stop)
US_SENSOR = EV3UltrasonicSensor(4)

def main():
    
    try:
        
        
        consecutive_low_values = 0  # Initialize the counter
        
        drumming.start()
        flute_start.start()
        while True:
            print("hello")
            us_data = US_SENSOR.get_value()
            print(us_data)
            if us_data < 8:
                consecutive_low_values += 1
                if consecutive_low_values >= 6:  # TIME_PERIOD is the number of consecutive low values required
                    EMERGENCY_STOP = True
                    print("Emergency Stop activated")
                    reset_brick()
                    exit()
            else:
                consecutive_low_values = 0 # Reset the counter if us_data is not low
            time.sleep(0.1)
    except KeyboardInterrupt as e:
        reset_brick()
        print(e)
        exit()
main()

# def main():
#     try:
#         emergency_stop.start()
#         flute_start.start()
#         drumming.start()
#     except BaseException:
#         pass
