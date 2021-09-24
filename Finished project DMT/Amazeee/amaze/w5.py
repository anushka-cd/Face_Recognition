import pyautogui
import time
distance=50
time.sleep(5)
pyautogui.click()
while(distance>0):
    pyautogui.dragRel(distance,0,duration=0.2)
    pyautogui.dragRel(0,distance,duration=0.2)
    distance-=20
    pyautogui.dragRel(-distance,0,duration=0.2)
    pyautogui.dragRel(0,-distance,duration=0.2)
    distance-=20
         
