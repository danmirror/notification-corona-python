import requests
from gtts import gTTS
from playsound  import playsound
from bs4 import BeautifulSoup
from plyer import notification
import time
import os

res = requests.get('https://www.worldometers.info/coronavirus/').text
soup = BeautifulSoup(res,'html.parser')
soup.encode('utf-8')

cases = soup.find("div",{"class": "maincounter-number"})
# print(cases)
cases_all = cases.get_text().strip()


def voice(message):
    #save mp3
    save = 'voicetry.mp3'

    mytext = 'total number of cases corona virus'+message
    language = 'en'

    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(save)

    playsound(save)
    #you can remove using this
    #os.remove(save)


def notifyme(title,message):
    notification.notify(
        title = title,
        message = message,
        timeout = 5
    )

while True:
    voice(cases_all)
    notifyme('total number of cases',cases_all)
    print('voice')
    time.sleep(10)