import pyautogui as spam
import time
i=1
participants=input("enter number of members: ")
time.sleep(2)
while i < int(participants):
    spam.typewrite("@")
    spam.press('down')
    spam.press('enter')
    i +=1