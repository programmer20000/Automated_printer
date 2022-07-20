from time import sleep

import pyautogui

folder_path = input("Enter folder path: ")

pyautogui.PAUSE = 2
pyautogui.FAILSAFE = True

pyautogui.hotkey('win','r')
pyautogui.write(folder_path)
pyautogui.press('Enter')
pyautogui.press('down')
pyautogui.press('Enter')
pyautogui.hotkey('ctrl','p')
pyautogui.click(146,975)
sleep(6)
pyautogui.click(146,975)
