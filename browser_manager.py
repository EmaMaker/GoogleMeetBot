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


G_ACCOUNT_MAIL = None
G_ACCOUNT_PASS = None

FIREFOX_DVD_DIR = "/usr/bin/geckodriver"

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
    global browser, G_ACCOUNT_MAIL, G_ACCOUNT_PASS

    print("Input your google account credentials. The information will not be stored anywhere and you will have to relogin everytime you restart this bot\n")
    G_ACCOUNT_MAIL = input("Type your email: ")
    G_ACCOUNT_PASS = input("Type your password: ")

    #webdriver.FirefoxProfile('/home/emamaker/Documents/Projects/GoogleMeetBot/firefox_profile')
    browser = webdriver.Firefox()

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

def loginIntoGoogle():
    global browser
    browser.get("https://myaccount.google.com/?utm_source=sign_in_no_continue")
    t.sleep(3)
    #we can use selectors in this webside, since they're static
    #login button
    clickButton(By.CSS_SELECTOR, "li.h-c-header__cta-li:nth-child(2) > a:nth-child(1)")
    #login with google
    #clickButton(By.CSS_SELECTOR, "button.s-btn__icon:nth-child(1)")
    #write email
    writeText(By.CSS_SELECTOR, "#identifierId", G_ACCOUNT_MAIL)
    t.sleep(3)
    #write pwd
    writeText(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input", G_ACCOUNT_PASS)
    t.sleep(3)

def loginIntoGoogleWithStackOverflow():
    global browser
    browser.get("https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f")
    t.sleep(3)
    #we can use selectors in this webside, since they're static
    #login with google
    clickButton(By.CSS_SELECTOR, "#openid-buttons > button.grid--cell.s-btn.s-btn__icon.s-btn__google.bar-md.ba.bc-black-100")
    #login button
    #write email
    writeText(By.CSS_SELECTOR, "#identifierId", G_ACCOUNT_MAIL)
    t.sleep(3)
    #write pwd
    writeText(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input", G_ACCOUNT_PASS)
    t.sleep(3)

def hangUpMeeting():
    clickButton(By.XPATH, HANG_UP_BTN_XPATH)
