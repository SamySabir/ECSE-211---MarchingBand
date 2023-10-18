#!/usr/bin/env python3

"""
Module to play sounds when the touch sensor is pressed.
This file must be run on the robot.
"""

import time
from utils import sound
from utils.brick import TouchSensor, wait_ready_sensors

NOTE_1 = sound.Sound(duration=0.3, pitch="A4", volume=90)
NOTE_2 = sound.Sound(duration=0.3, pitch="B4", volume=90)
NOTE_3 = sound.Sound(duration=0.3, pitch="C5", volume=90)
NOTE_4 = sound.Sound(duration=0.3, pitch="E5", volume=90)
TOUCH_SENSOR_1 = TouchSensor(1)
TOUCH_SENSOR_2 = TouchSensor(2)
TOUCH_SENSOR_3 = TouchSensor(3)


wait_ready_sensors() # Note: Touch sensors actually have no initialization time


def play_note_1():
    "Play a single note."
    NOTE_1.play()
    NOTE_1.wait_done()

def play_note_2():
    "Play a single note."
    NOTE_2.play()
    NOTE_2.wait_done()

def play_note_3():
    "Play a single note."
    NOTE_3.play()
    NOTE_3.wait_done()


def play_note_4():
    "Play a single note."
    NOTE_4.play()
    NOTE_4.wait_done()


def play_sound_on_button_press():
    "In an infinite loop, play a single note when the touch sensor is pressed."
    try:
            
            state1 = False
            state2 = False
            state3 = False
            
            for i in range(100):
                state1 += TOUCH_SENSOR_1.is_pressed()
                state2 += TOUCH_SENSOR_2.is_pressed()
                state3 += TOUCH_SENSOR_3.is_pressed()
            
            if (state1 and state2):
                play_note_4()
            elif state1:
                play_note_1()
            elif state2:
                play_note_2()
            elif state3:
                play_note_3()
            
    except BaseException:  # capture all exceptions including KeyboardInterrupt (Ctrl-C)
        exit()


if __name__=='__main__':

    # TODO Implement this function
    while True:
        play_sound_on_button_press()
