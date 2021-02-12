import sys
import selenium
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import os
from enum import Enum
import threading
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import time as t
from utils import *


'''Locating by xpath here is the best thing to do here, since google Meet changes selectors, classes name and all that sort of stuff for every meeting
    XPaths remaing the same, but a slight change by them would make this program fail.
    The xpath is found clicking by inspecting the element of the searched button, and finding the parent div tthat has role="button" tag
'''

MIC_XPATH = '/html/body/div[1]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div/div/div'
WEBCAM_XPATH = '/html/body/div[1]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/div'
JOIN_XPATH = '/html/body/div[1]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div/div[1]'
OPTION_XPATH = '/html/body/div[1]/c-wiz/div/div/div[6]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div'

CHAT_BTN_XPATH = '/html/body/div[1]/c-wiz/div[1]/div/div[6]/div[3]/div[6]/div[3]/div/div[2]/div[3]'
CHAT_SELECTCHAT_BTN_XPATH = '/html/body/div[1]/c-wiz/div[1]/div/div[6]/div[3]/div[3]/div/div[2]/div[2]/div[1]/div[2]'

#Using tagname for text area because xpath doesn't really work, and we're sure it's the only textarea on the webpage
CHAT_TEXT_XPATH = "textarea"

HANG_UP_BTN_XPATH = '/html/body/div[1]/c-wiz/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[2]/div'

CHAT_CLOSE_BTN_XPATH = '/html/body/div[1]/c-wiz/div[1]/div/div[6]/div[3]/div[3]/div/div[2]/div[1]/div[2]/div/button'

browser = None

def initFirefox():
    global browser

    browser = webdriver.Firefox(firefox_profile=webdriver.FirefoxProfile(FIREFOX_PROFILE), executable_path=FIREFOX_DVD_DIR)

def joinMeeting(link):
    global browser

    if link == '':
        return

    try:
        browser.get(link)
        t.sleep(15)
        print("Trying to join meeting")
        clickButton(By.XPATH, MIC_XPATH)
        clickButton(By.XPATH, WEBCAM_XPATH)
        clickButton(By.XPATH, JOIN_XPATH)
    except:
        # In this way, in case of any error we can try again
        print("Failed to join meeting, trying again in 60 secs")
        t.sleep(60)
        joinMeeting(link)


def clickButton(by, selector):
    global browser
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((by, selector))).click()
    t.sleep(1)

def writeText(by, selector, text):
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((by, selector))).clear()
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((by, selector))).send_keys(text + "\n")

def sendChatMsg(text):
    global browser

    #open chat menu
    clickButton(By.XPATH, CHAT_BTN_XPATH)
    #select chat option
    clickButton(By.XPATH, CHAT_SELECTCHAT_BTN_XPATH)
    #write msg
    writeText(By.TAG_NAME, CHAT_BTN_XPATH, text)
    t.sleep(1)
    #close chat
    clickButton(By.XPATH, CHAT_CLOSE_BTN_XPATH)


def checkStarted():
    try:
        clickButton(By.XPATH, OPTION_XPATH)
    except:
        return False
    return True

def hangUpMeeting():
    try:
        clickButton(By.XPATH, HANG_UP_BTN_XPATH)
    except:
        return False
    return True
