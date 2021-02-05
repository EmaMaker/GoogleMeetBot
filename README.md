# GoogleMeetBot
A bot to automatically join Google Meet meetings at the correct time


## How it works
The bot automates a FireFox session using Python and Selenium.<br>
It joins the programmed google meetings automatically, with microphone and webcam disabled.<br>
It uses the **schedule** python module to automatically access and close meetings at the given time, it can only join one meeting at the time<br>
Normally Google Accounts are not allowed to be logged in when using an automated browser, but logging in via stackoverflow.com worksaround this problem<br>
In case this is not working, you can disable such security feature in your google account settings. Some business and enterprise account may not have this problem by default

## Dependencies
All python deps are listed in **requirements.txt**, just run<br>
    pip install -r requirements.txt

## Add your own meetings
To add your own  meetings into **meetings.py**, adding another <em>scheduleMeeting</em> line like the one already present. You can add as many as you want, but remember that this bot does not support joining multiple meetings at the same time

