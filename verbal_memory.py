#"Hello World"(print)

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import keyboard

# Open chromes
driver = webdriver.Chrome()
driver.get("https://humanbenchmark.com/tests/verbal-memory")

# Time for login or sign up - You should be fast af
time.sleep(20)

# Starts the Challenge
start_button = driver.find_element(By.CLASS_NAME,"css-1bnidmp")
start_button.click()

# The new words will be stored in here 
l=[]

# For Keyboard enable and disable
clicking_Enabled = True

def Toggle_Clicking():
  global clicking_Enabled
  clicking_Enabled = not clicking_Enabled
  
# Hotkey to activate or deactivate
keyboard.add_hotkey('ctrl+q',Toggle_Clicking)

# Main thing
try:
  while True:
    if not clicking_Enabled:
      time.sleep(0.1)
      continue
    
    # Finds the word
    words_element = driver.find_element(By.CLASS_NAME,"word")
    words = words_element.text
    
    # checks if the word is there or not 
    if words not in l:
      l.append(words)
      new_button = driver.find_element(By.XPATH,'//button[text()="NEW"]')
      new_button.click()
    else:
      seen_button = driver.find_element(By.XPATH,'//button[text()="SEEN"]')
      seen_button.click()

except Exception as e:
  print(e)
  
# So that if hotkey activate or deactivate it should wait instead of closing it
keyboard.wait()
time.sleep(20)
driver.quit()