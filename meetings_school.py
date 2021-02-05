import time as t
import schedule
import browser_manager

''' STORE MEET LINKS HERE'''
MATHS = 'https://meet.google.com/lookup/fn2tkngzid?authuser=0&hs=179'
LITERATURE = 'https://meet.google.com/lookup/bhoqky4qee?authuser=0&hs=179'
ENGLISH = 'https://meet.google.com/lookup/hlj4rhyj4p?authuser=0&hs=179'
ELECTRONICS = 'https://meet.google.com/lookup/ehuwfglxvr?authuser=0&hs=179'
SYSTEMS = ''
TPSEE = 'https://meet.google.com/lookup/bc4r2d32ua?authuser=0&hs=179'
TPSEE_ELT = 'https://meet.google.com/lookup/gdaq3kmguh?authuser=0&hs=179'
TPSEE_SYS = 'https://meet.google.com/lookup/gdaq3kmguh?authuser=0&hs=179'
ELT_SYSTEMS = ''


'''TIME SCHEDULE - START AND FINISH'''
FIRST_HOUR = "8:00"
SECOND_HOUR = "8:50"
THIRD_HOUR = "9:50"
FOURTH_HOUR = "10:50"
FIFTH_HOUR = "11:50"
SIXTH_HOUR = "12:40"
SEVENTH_HOUR = "13:40"

def setup_schedule():
    #scheduleMeeting("friday", "20:56", "20:57", "https://meet.google.com/jqn-fgav-aad")

    # Monday schedule
    scheduleMeeting("monday", FIRST_HOUR, SECOND_HOUR, TPSEE)
    scheduleMeeting("monday", SECOND_HOUR, THIRD_HOUR, ENGLISH)
    scheduleMeeting("monday", THIRD_HOUR, FOURTH_HOUR, SYSTEMS)
    scheduleMeeting("monday", FOURTH_HOUR, FIFTH_HOUR, MATHS)
    scheduleMeeting("monday", FIFTH_HOUR, SEVENTH_HOUR, LITERATURE)

    # Tuesday schedule
    scheduleMeeting("tuesday", FIRST_HOUR, THIRD_HOUR, SYSTEMS)
    scheduleMeeting("tuesday", THIRD_HOUR, FIFTH_HOUR, ELECTRONICS)
    scheduleMeeting("tuesday", FIFTH_HOUR, SIXTH_HOUR, TPSEE_ELT)
    scheduleMeeting("tuesday", SIXTH_HOUR, SEVENTH_HOUR, TPSEE)

    # Wednesday schedule
    scheduleMeeting("wednesday", FIRST_HOUR, SECOND_HOUR, ELT_SYSTEMS)
    scheduleMeeting("wednesday", SECOND_HOUR, THIRD_HOUR, MATHS)
    scheduleMeeting("wednesday", THIRD_HOUR, FOURTH_HOUR, LITERATURE)
    scheduleMeeting("wednesday", SIXTH_HOUR, SEVENTH_HOUR, LITERATURE)

    # Thursday schedule
    scheduleMeeting("thursday", FIRST_HOUR, SECOND_HOUR, ELECTRONICS)
    scheduleMeeting("thursday", SECOND_HOUR, THIRD_HOUR, ENGLISH)
    scheduleMeeting("thursday", FOURTH_HOUR, FIFTH_HOUR, TPSEE)
    scheduleMeeting("thursday", FIFTH_HOUR, SIXTH_HOUR, TPSEE_SYS)
    scheduleMeeting("thursday", SIXTH_HOUR, SEVENTH_HOUR, SYSTEMS)

    # Friday schedule
    scheduleMeeting("friday", FIRST_HOUR, SECOND_HOUR, MATHS)
    scheduleMeeting("friday", SECOND_HOUR, THIRD_HOUR, ENGLISH)
    scheduleMeeting("friday", FOURTH_HOUR, FIFTH_HOUR, LITERATURE)
    scheduleMeeting("friday", FIFTH_HOUR, SIXTH_HOUR, LITERATURE)
    scheduleMeeting("friday", SIXTH_HOUR, SEVENTH_HOUR, TPSEE)

def scheduleMeeting(day, startHour, endHour, link):
    if str(day).lower() == "monday":
        schedule.every().monday.at(startHour).do(browser_manager.joinMeeting, link)
        schedule.every().monday.at(endHour).do(browser_manager.hangUpMeeting)
    elif str(day).lower() == "tuesday":
        schedule.every().tuesday.at(startHour).do(browser_manager.joinMeeting, link)
        schedule.every().tuesday.at(endHour).do(browser_manager.hangUpMeeting)
    elif str(day).lower() == "wednesday":
        schedule.every().wednesday.at(startHour).do(browser_manager.joinMeeting, link)
        schedule.every().wednesday.at(endHour).do(browser_manager.hangUpMeeting)
    elif str(day).lower() == "thursday":
        schedule.every().thursday.at(startHour).do(browser_manager.joinMeeting, link)
        schedule.every().thursday.at(endHour).do(browser_manager.hangUpMeeting)
    elif str(day).lower() == "friday":
        schedule.every().friday.at(startHour).do(browser_manager.joinMeeting, link)
        schedule.every().friday.at(endHour).do(browser_manager.hangUpMeeting)
    elif str(day).lower() == "saturday":
        schedule.every().saturday.at(startHour).do(browser_manager.joinMeeting, link)
        schedule.every().saturday.at(endHour).do(browser_manager.hangUpMeeting)
    elif str(day).lower() == "sunday":
        schedule.every().sunday.at(startHour).do(browser_manager.joinMeeting, link)
        schedule.every().sunday.at(endHour).do(browser_manager.hangUpMeeting)
