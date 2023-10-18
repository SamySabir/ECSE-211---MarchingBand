"""
This is the implementation of the EmergencyStopSystem. When the US sensor detects noise at a certain interval distance from it,
it will stop all functions.
"""

from utils.brick import EV3UltrasonicSensor, wait_ready_sensors, reset_brick
from time import sleep

DELAY_SEC = 0.01
EMERGENCY_STOP = False

print("Program start. \nWaiting for sensor to turn on...")

US_SENSOR = EV3UltrasonicSensor(4)


wait_ready_sensors(True) #Shows what the robot is trying to initialize
print("Done waiting.")


def emergency_stop():
    try:
        consecutive_low_values = 0  # Initialize the counter
        while True:
            print(1)
            us_data = US_SENSOR.get_value()
            if us_data < 5:
                consecutive_low_values += 1
                if consecutive_low_values >= 10:  # TIME_PERIOD is the number of consecutive low values required
                    EMERGENCY_STOP = True
                    print("Emergency Stop activated")
                    reset_brick()
                    exit()
            else:
                consecutive_low_values = 0  # Reset the counter if us_data is not low
            sleep(DELAY_SEC)
    except BaseException:
        pass

if __name__ == "__main__":
    emergency_stop()