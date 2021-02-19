from cv2 import cv2
import numpy as np
import pyautogui
import time
import os
import pynput


def record_screen():
    while True:
        frame = pyautogui.screenshot(region=(545, 200, 360, 400))
        frame = np.array(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        get_image_data(frame)


def get_image_data(frame):
    lower = np.array([0, 0, 0])
    upper = np.array([50, 50, 100])
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    frame = cv2.inRange(frame, lower, upper)
    play_piano(frame)


def play_piano(frame):
    matches = np.argwhere(frame == 255)
    if len(matches) == 0:
        pass
    else:
        place_to_click_x = matches[-1][-1]
        place_to_click_x += 545
        place_to_click_y = matches[-1][0]
        place_to_click_y += 200
        #print(f"X: {place_to_click_x} Y: {place_to_click_y}")
        mouse.position = (place_to_click_x, place_to_click_y)
        mouse.press(button=pynput.mouse.Button.left)
        time.sleep(0.01)
        mouse.release(button=pynput.mouse.Button.left)


def quit_when_escape(key):
    if key == pynput.keyboard.Key.esc:
        os._exit(0)


if __name__ == '__main__':
    mouse = pynput.mouse.Controller()
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

# bot dziala tylko na https://www.gry.pl/gra/magiczne-klawisze-pianina i przegladarka musi byc wlaczona w pelnym oknie
