import threading
import time
import EmergencyStopDesign
import speaker_button 
from drum_class_and_test import drummer
flute_start = threading.Thread(target=speaker_button.flute)
drumming = threading.Thread(target=drummer)
#emergency_stop = threading.Thread(target=EmergencyStopDesign.emergency_stop)

def main():
    try:
        consecutive_low_values = 0  # Initialize the counter
        
        drumming.start()
        flute_start.start()
        while True:
            print("hello")
            us_data = US_SENSOR.get_value()
            print(us_data)
            if us_data < 5:
                consecutive_low_values += 1
                if consecutive_low_values >= 10:  # TIME_PERIOD is the number of consecutive low values required
                    EMERGENCY_STOP = True
                    print("Emergency Stop activated")
                    reset_brick()
                    break
            else:
                consecutive_low_values = 0 # Reset the counter if us_data is not low
            sleep(0.1)
    except BaseException:
        pass
main()

# def main():
#     try:
#         emergency_stop.start()
#         flute_start.start()
#         drumming.start()
#     except BaseException:
#         pass
