import pyautogui
import random
import time
import pyperclip
email = "flexy06@outlook.de"
text = "r"
anzahl_email_adressen = 6
emails = ["your email", "your email", "your email", "your email", "your email","your email","your email"]
screenWidth, screenHeight = pyautogui.size()
pyautogui.FailSafeException
#pyautogui.moveTo(250, 50)
#pyautogui.click()
#pyautogui.alert('Start rewards point generator?')
#pyautogui.click('edit.png')
#print(res)


def tab(n):
    time.sleep(1)
    for i in range(n):
        pyautogui.press("Tab")
        time.sleep(0.1)


def log_out_in(emailaddress, counter):
    pyautogui.click(1580, 120)  # profile
    time.sleep(0.6)
    pyautogui.click(1760, 200)  # sign out
    time.sleep(1.8)
    pyautogui.click(1650, 120)  # sign in
    time.sleep(0.4)
    pyautogui.click(800, 510)
    time.sleep(1.0)
    pyautogui.click(800, 510)
    pyautogui.hotkey('ctrl', 'a')
    pyperclip.copy(emailaddress)
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'v')
    tab(4)
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(0.6)
    pyautogui.press("enter")
    time.sleep(0.2)
    pyautogui.keyDown('enter')
    time.sleep(0.2)
    pyautogui.keyDown('enter')
    time.sleep(0.2)
    pyautogui.keyDown('enter')


    #pyautogui.click(1050, 660) #weiter
    #pyautogui.click(1050, 690) #sign in
    #pyautogui.click(900, 730)
    #pyautogui.click(900, 640)
    #pyautogui.click(1050, 690)


def rewardsredeem(text):
    # pyautogui.moveTo(250, 50)
    # pyautogui.click()
    # pyautogui.alert('Start rewards point generator?')
    # pyautogui.click('edit.png')
    # print(res)
    pyautogui.click(900, 730)
    pyautogui.click(900, 640)

    for i in range(0, 45):
        text += str(random.randint(0, 9))

        pyautogui.click(250, 50)
        if i < 8:
            pyautogui.write(text, interval=0.08 - (i / 100))
        else:
            pyautogui.write(text, interval=0.0)
        pyautogui.press('enter')

for i in range(0, len(emails)):

    log_out_in(emails[i], i)
    time.sleep(1.2)
    rewardsredeem(text)
    time.sleep(2.0)




    #email = "*******"
    #log_out_in(email)
    #time.sleep(1.2)
    #rewardsredeem(text)
    #time.sleep(2.0)
    #email = "*********"
    #log_out_in(email)
    #time.sleep(1.2)
    #rewardsredeem(text)




#pyautogui.press("Tab")
#pyautogui.click(800, 510)
"""pyautogui.click(1580, 120) #profile
    time.sleep(0.6)
    pyautogui.click(1760, 200) #sign out
    time.sleep(1.8)
    pyautogui.click(1650, 120) #sign in
    time.sleep(0.4)
    pyautogui.click(800, 510)
    time.sleep(1.0)
    pyautogui.click(800, 510)
    pyautogui.hotkey('ctrl', 'a')
    pyperclip.copy(emailaddress)
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'v')
    tab(4)
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(0.6)
    pyautogui.press("enter")
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.keyDown('enter')
    time.sleep(0.2)
    pyautogui.keyDown('enter')
    pyautogui.click()"""
