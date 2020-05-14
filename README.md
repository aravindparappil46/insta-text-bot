
# Instagram Direct Message Bot

Automatically sends direct messages to a Instagram user whom you follow!

Each message is sent one word at a time!


## Requirements

- Must have ```python3``` installed

- Must have selenium installed. Do `pip install selenium`

- ```ChromeDriver``` based on the version of Google Chrome you are running. Go [here](https://chromedriver.chromium.org/downloads) to download

- A file containing the message you want to send (can be in any format)

- An Instagram account :/

## How-to

- Fill up the details in ```settings.ini```

- Open up a terminal and run ``` python3 bot.py 0```  (or ```python bot.py 0``` depending on your environment setup. The code is written in Python 3)

- Change the 0 to 1 if you log in to your Instagram account via Facebook and not using Instagram credentials

- Watch it work!

**Warning:** ```settings.ini``` contains plain-text passwords which is not a safe approach. For now, it is **your responsibility** to ensure its safety. Don't store this file where other's can easily access. Please feel free to fork and raise a PR if you want to contribute a safer approach to fetching credentials.<br><br>
**Note:** This was for educational purposes only. Spamming is not fun & never encouraged. I claim no responsibility over how it's used nor over the safety and security of the credentials stored in ```settings.ini```
