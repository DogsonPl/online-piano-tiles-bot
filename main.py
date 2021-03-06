from cv2 import cv2
import numpy as np
import pyautogui
import time
import os
import pynput


class UserInputListener:
    def start_listening(self):
        listener = pynput.keyboard.Listener(on_press=self.check_input)
        listener.start()

    @staticmethod
    def check_input(key):
        if key == pynput.keyboard.Key.esc:
            os._exit(0)


class GetInfoFromScreen:
    def __init__(self):
        self.lower_color = np.array([0, 0, 0])
        self.upper_color = np.array([50, 50, 100])
        self.play_piano = PlayPiano()

    def start(self):
        self.play_piano.start()
        self.record_screen()

    def record_screen(self):
        while True:
            frame = pyautogui.screenshot(region=(LEFT, TOP, WIDTH, HEIGHT))
            frame = np.array(frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.get_image_data(frame)

    def get_image_data(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
        frame = cv2.inRange(frame, self.lower_color, self.upper_color)
        self.play_piano.play_piano(frame)


class PlayPiano:
    def __init__(self):
        self.mouse = pynput.mouse.Controller()

    def start(self):
        self.press_button(780, 450)
        time.sleep(1)

    def play_piano(self, frame):
        matches = np.argwhere(frame == 255)
        if len(matches) == 0:
            pass
        else:
            place_to_click_x = matches[-1][-1]
            place_to_click_x += LEFT
            place_to_click_y = matches[-1][0]
            place_to_click_y += TOP
            self.press_button(place_to_click_x, place_to_click_y)

    def press_button(self, place_to_click_x, place_to_click_y):
        self.mouse.position = (place_to_click_x, place_to_click_y)
        self.mouse.press(button=pynput.mouse.Button.left)
        time.sleep(0.09)
        self.mouse.release(button=pynput.mouse.Button.left)


def start():
    UserInputListener().start_listening()
    timer = 5
    print("Click ESC to close program")
    for i in range(5):
        print(f"Starting in {timer}", end="\r")
        timer -= 1
        time.sleep(1)
    print("Started! Press escape to stop program")
    GetInfoFromScreen().start()


if __name__ == '__main__':
    LEFT = 545
    TOP = 200
    WIDTH = 360
    HEIGHT = 400
    start()

# bot works only on https://www.agame.com/game/magic-piano-tiles
