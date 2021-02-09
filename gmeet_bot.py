'''Automatically join Google Meet meetings, with muted camera and mic
Can write in chat'''

import meetings
import browser_manager
import schedule
import time

browser_manager.initFirefox()
meetings.setup_schedule()

while True:
    schedule.run_pending()
    time.sleep(1)