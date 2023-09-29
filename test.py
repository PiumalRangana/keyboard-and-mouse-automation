import pyautogui

pyautogui.click(75,746)
pyautogui.write("notepad")
pyautogui.countdown(3)
pyautogui.press("enter")
pyautogui.countdown(3)
pyautogui.write("This message is written by PyAutoGui program...")
pyautogui.countdown(2)
pyautogui.hotkey("ctrl","s")

pyautogui.countdown(3)
pyautogui.press(["left","left","left","left","backspace"])
pyautogui.countdown(2)
pyautogui.write("PyAutoGui_program")
pyautogui.press("enter")

pyautogui.hotkey("alt","f4")
print("done")