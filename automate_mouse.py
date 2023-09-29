import pyautogui

#Open the paint app
pyautogui.click(74,745)
pyautogui.countdown(2)
pyautogui.write("paint")
pyautogui.countdown(1)
pyautogui.press("enter")
pyautogui.countdown(1)

#pyautogui.moveTo(682.5,383.5)

def first_triangle():
    distance = 250
    while distance > 0:
        pyautogui.drag(distance,0)
        pyautogui.drag(0,distance)
        distance -=5
        pyautogui.drag(-distance,-distance)
        distance -= 5



def second_triangle():
    distance=250
    while distance > 0:
        pyautogui.drag(-distance,0)
        pyautogui.drag(0,-distance)
        distance -=5
        pyautogui.drag(distance,distance)
        distance -= 5

def squer():
    first_triangle()
    pyautogui.drag(125,125)
    second_triangle()

pyautogui.moveTo(13,156)
def pattern():
    for _ in range(2):
        squer()
        pyautogui.drag(125,125)
        squer()
        pyautogui.move(125,-375)
    squer()

pattern()

#save the painting
pyautogui.hotkey("alt","f4")
pyautogui.countdown(1)
pyautogui.press("enter")
pyautogui.countdown(1)
pyautogui.press("backspace")
pyautogui.countdown(1)
pyautogui.write("PyAutoGui_painting")
pyautogui.press("enter")