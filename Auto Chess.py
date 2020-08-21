import pyautogui, time
from pynput.keyboard import Key, Controller


def clientQueue():
    pyautogui.click(820, 915)  # Find Match Button

    # Presses accept button 60 times.
    for i in range(140):
        pyautogui.click(960, 750)  # Accept Button
        time.sleep(1)


def gameBait():
    # Tries to confirm surrender 30 times.
    for i in range(30):
        time.sleep(10)

        pyautogui.click(149, 266, button='right')
        time.sleep(1)

        keyboard = Controller()

        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(1)
        pyautogui.click(149, 266, button='right')

        time.sleep(1)
        keyboard.press('/')

        keyboard.release('/')
        time.sleep(1)
        keyboard.press('f')
        keyboard.release('f')
        time.sleep(1)
        keyboard.press('f')
        keyboard.release('f')

        time.sleep(1)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(1)

        pyautogui.click(850, 605)  # Confirm Button
        pyautogui.dragTo(850, 605)
        time.sleep(1)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        time.sleep(10)


def playAgain():
    time.sleep(1)
    pyautogui.click(850, 940)  # Play Again Button
    time.sleep(1)


numOfGames = int(input("How many games do you want completed?\n"))
print("This will take around " + str(numOfGames * 11) + " minutes to complete")


for temp in range(numOfGames):
    clientQueue()
    time.sleep(5)
    gameBait()
    time.sleep(1)
    playAgain()
    time.sleep(4)
