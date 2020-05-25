"""Not work well at the time of transition of day to night."""



import pyautogui
from PIL import ImageGrab
import time

# Functions
def press_key(key):
    return pyautogui.keyDown(key)


def take_screenshot():
    """Take the Screenshot and return the grey scale image"""
    image = ImageGrab.grab().convert("L")
    return image


def isObsticle(data):
    """
    Find obsticle(i.e., cactus and bird) and action according to the obsticle.

    :param data: Screenshot data of the game
    :return: An action
    """
    # Box for Birds
    for x in range(345, 335, -1):
        for y in range(370, 310, -1):
            if 180 > data[x, y] > 80:
                press_key("down")
                time.sleep(0.5)
                return pyautogui.keyUp("down")


    # Box for cactus
    for x in range(345, 325, -1):
        for y in range(455, 390, -1):
            if 180 > data[x, y] > 80:
                press_key("space")
                return
    return False


if __name__ == '__main__':
    time.sleep(2)
    print("Game starts now....")
    pyautogui.click(x=300, y=400) # Click to start the dino game

    while True:
        img = take_screenshot()
        data = img.load()
        isObsticle(data)
