import pyautogui as bot
import time as sleep


def click(x, y):
    bot.moveTo(x, y,  duration=1, tween=bot.easeInOutQuad)
    bot.click()


def checkScreen():
    buttonAccept = bot.locateOnScreen('accept_game.png', confidence=0.7)

    if buttonAccept != None:
        click(buttonAccept.left, buttonAccept.top)
        return True
    return False


def main():
    while True:
        if checkScreen():
            sleep(6)


main()
