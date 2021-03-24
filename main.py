from cv2 import cv2
import numpy as np
import pyautogui
import time
import os
import pynput

# todo add automatically click start


def record_screen():
    while True:
        frame = pyautogui.screenshot(region=(LEFT, TOP, WIDTH, HEIGHT))
        frame = np.array(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        get_image_data(frame)


def get_image_data(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    frame = cv2.inRange(frame, LOWER_COLOR, UPPER_COLOR)
    play_piano(frame)


def play_piano(frame):
    matches = np.argwhere(frame == 255)
    if len(matches) == 0:
        pass
    else:
        place_to_click_x = matches[-1][-1]
        place_to_click_x += LEFT
        place_to_click_y = matches[-1][0]
        place_to_click_y += TOP
        #print(f"X: {place_to_click_x} Y: {place_to_click_y}")
        MOUSE.position = (place_to_click_x, place_to_click_y)
        MOUSE.press(button=pynput.mouse.Button.left)
        time.sleep(0.01)
        MOUSE.release(button=pynput.mouse.Button.left)


def quit_when_escape(key):
    if key == pynput.keyboard.Key.esc:
        os._exit(0)


if __name__ == '__main__':
    MOUSE = pynput.mouse.Controller()
    LOWER_COLOR = np.array([0, 0, 0])
    UPPER_COLOR = np.array([50, 50, 100])
    LEFT = 545
    TOP = 200
    WIDTH = 360
    HEIGHT = 400

    listener = pynput.keyboard.Listener(on_press=quit_when_escape)
    listener.start()
    timer = 5
    print("Click ESC to close program")
    for i in range(5):
        print(f"Starting in {timer}", end="\r")
        timer -= 1
        time.sleep(1)
    print("Started! Press escape to stop program")

    record_screen()

# bot works only on https://www.agame.com/game/magic-piano-tiles
