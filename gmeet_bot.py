'''Automatically join Google Meet meetings, with muted camera and mic
    Just give link and it joins. Features chat too
    Planning on adding a schedule system'''

import meetings
import browser_manager
import schedule
import time

browser_manager.initFirefox()
browser_manager.loginIntoGoogleWithStackOverflow()
#while checkStarted() is False:
#browser.sendChatMsg("hello world")

meetings.setup_schedule()

while True:
    schedule.run_pending()
    time.sleep(1)