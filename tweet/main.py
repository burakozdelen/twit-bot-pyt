from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random
import time
import pyautogui
import pyperclip
a = 0
pyperclip.copy("#") # Enter the Tweet
def start():
    driver = webdriver.Chrome()
    driver.get("https://twitter.com/i/flow/login")
    time.sleep(6)
    u_name = driver.find_element("xpath" , '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
    u_name.send_keys("mart152023") # Enter your Twitter username
    u_name.send_keys(Keys.ENTER)
    time.sleep(2)
    pyautogui.write("1234567890fb") # Enter your twitter password
    pyautogui.press('enter')
    time.sleep(6)
    b = random.randint(1, 99999)
    while (a==0):
        time.sleep(1)
        driver.get("https://twitter.com/compose/tweet")
        time.sleep(2)
        msj = f" {b} "
        pyautogui.hotkey("ctrl","v")
        pyautogui.write(str(msj))
        b+=1
        tweetle = driver.find_element("xpath" , '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span')
        actions = ActionChains(driver)
        actions.move_to_element(tweetle).click().perform()
    isim= input()
start()