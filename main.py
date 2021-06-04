import time
import sys
import threading 
from pynput.mouse import Button, Controller 
from pynput.keyboard import Listener, KeyCode 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

browser  = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://kingofkfcjamal.github.io/CaseClicker/')

targetStr = input("what is the target amount? >")
target = int(targetStr)
input("enter to start")

ctButton = browser.find_element_by_xpath("//*[@id=\"coinTab\"]")
ctButton.click()

while (True):
    walletPath = browser.find_element_by_xpath("//*[@id=\"money\"]").text
    walletStr = walletPath[1:]
    wallet = int(float(walletStr))
    toSpend = wallet / 4
    if wallet >= target:
        exit()
    else:
        coin = browser.find_element_by_xpath("//*[@id=\"btnFlip\"]")
        coin.click()
        browser.switch_to.alert.accept()
        time.sleep(0.1)
        browser.switch_to.alert.send_keys(str(toSpend))
        browser.switch_to.alert.accept()

        time.sleep(0.1)
        browser.switch_to.alert.send_keys("T")
        browser.switch_to.alert.accept()
