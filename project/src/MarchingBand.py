import threading
import time
import EmergencyStopDesign

flute = threading.Thread(target=function)
drumming = threading.Thread(target=function)
emergency_stop = threading.Thread(target=EmergencyStopDesign.emergency_stop())

def main():
    try:
        while True:
            #checking for emergency stop
            emergency_stop.start()
            if (EmergencyStopDesign.EMERGENCY_STOP):
                #stop subsystems
            else:
                flute.start()
                drumming.start()

            time.sleep(0.01)

