from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time

# Open chromes
driver = webdriver.Chrome()
driver.get("https://humanbenchmark.com/tests/reactiontime")

# Time for login or sign up - You should be fast af
time.sleep(30)

# Starts the game
start_test = driver.find_element(By.CLASS_NAME,"view-splash")
start_test.click()
i = 1
while i<=5:
  try:
    # CLicks when Green appears 
    green_click = WebDriverWait(driver,1,poll_frequency=0.001).until(
      EC.presence_of_element_located((By.CLASS_NAME,"view-go"))
    )
    pyautogui.click(799,796)
    continue_test = driver.find_element(By.CLASS_NAME,"view-result")
    continue_test.click()
    i +=1
  except:
    pass
  
# Quits the browser 
time.sleep(20)
driver.quit()