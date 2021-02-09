# GoogleMeetBot
A bot to automatically join Google Meet meetings at the correct time


## How it works
The bot automates a FireFox session using Python, Selenium and the Geckdriver.<br>
It joins the programmed google meetings automatically, with microphone and webcam disabled.<br>
It uses the **schedule** python module to automatically access and close meetings at the given time, it can only join one meeting at the time<br>
Normally Google Accounts are not allowed to be logged in when using an automated browser, and this bot is no exception. 
The procedure described in **Using your account** is used to bypass this protection mechanism <br>

## Using your account
This login procedure is needed in order to bypass Google not allowing automated browsers to log in into accounts.<br><br>
**Preparation:**<br>
1. First of all install Mozilla FireFox from <https://www.mozilla.org/en-US/firefox/download/thanks/>.<br>
2. Download and install the Geckdriver for your OS from Mozilla's GitHub repo <https://github.com/mozilla/geckodriver/releases>.<br>
3. If you're using Linux, your package manager may have a package for that, so check that.<br>
4. Replace **FIREFOX_DVD_DIR** in **utils.py** with the path to the GeckoDriver executable you just installed.<br>

**Log in into your Google Account:**<br>
1. Open FireFox and go to *about:profiles*<br>
2. Click *Create a New Profile>Next* name it whatever you want then click *Finish*<br>
3. Search for the profile you just created in the list below, copy the *Root Directory* and paste it into **FIREFOX_PROFILE** into **utils.py**<br>
4. Now FireFox will have made the profile you just created the default one, so set the default profile back to what it was before<br>
5. Go the the profile you just created and click *Launch profile in new browser*. This will open a new FireFox window using your profile.<br>
6. In the new FireFox window just appeared, head over to gmail.com and log in into your Google account.<br>
7. Once logged in, the profile is ready to be used in this bot<br>


## Dependencies
All python deps are listed in **requirements.txt**, just run<br>
    pip install -r requirements.txt

## Add your own meetings
To add your own  meetings into **meetings.py**, adding another <em>scheduleMeeting</em> line like the one already present. You can add as many as you want, but remember that this bot does not support joining multiple meetings at the same time

