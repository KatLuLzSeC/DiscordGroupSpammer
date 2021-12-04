import keyboard
import pyautogui
c = True
while c:
    if keyboard.is_pressed('q'): break #click q to break operation
    pyautogui.click(47,167) 
    pyautogui.click(358,381)
    pyautogui.click(867,546)
    pyautogui.click(862,586)
    pyautogui.click(0,0) #edit this value to ur correct value
