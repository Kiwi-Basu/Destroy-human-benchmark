#"Hello World"(print)
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pyautogui
import keyboard

# Open chromes
driver = webdriver.Chrome()
driver.get("https://humanbenchmark.com/tests/aim")

# Time for login or sign up - You should be fast af
time.sleep(20)

# Area of the main test
region = (408,327,1141,533)

screen = pyautogui.screenshot(region=region)
screen.save("aim_screen.png")

target_color = (149,195,232) # Target color
stop_color = (255,209,84) # to stop The test color 

width,height = screen.size

# Keyboard Stop if Something CRAZZZZY happens
Clicking_Enabled = True
def Toggle_Clicking():
  global Clicking_Enabled
  Clicking_Enabled = not Clicking_Enabled
  
keyboard.add_hotkey('ctrl+q',Toggle_Clicking)

try:
  while True:
    if not Clicking_Enabled:
      time.sleep(0.1)
      continue
    
    screen = pyautogui.screenshot(region=region)
    width,height = screen.size
    found = False
    
    for y in range(0,height,35):
      for x in range(0,width,35):
        if screen.getpixel((x,y)) == target_color:
          screen_x = region[0] + x
          screen_y = region[1] + y
          pyautogui.click(screen_x,screen_y)
          found = True
          break
        
        if screen.getpixel((x,y)) == stop_color:
          Clicking_Enabled = False
          found = True
          break
      if found:
        break

except Exception as e:
  print(e)

# So that if hotkey activate or deactivate it should wait instead of closing it
keyboard.wait()
time.sleep(10)
driver.quit()
