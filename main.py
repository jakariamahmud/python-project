import pyautogui as pt
import time

limit = int(input("enter limite here: "))
message = input("enter message here: ")

count = 0;

time.sleep(5)
while count < limit:
    pt.typewrite(message)
    pt.press("enter")
    count += 1