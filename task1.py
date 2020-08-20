# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 16:37:29 2020

@author: hp
"""

import pyttsx3 as ts
import os

ts.speak('welcome ,what task i can perform for you')
initiate = ['open', 'run', 'start', 'excute', 'begin', 'play']
terminate = ['stop', 'exit', 'terminate', 'quit', 'left', 'bye']
browser = ['web', 'web browser', 'chrome', 'chrome browser', 'browser']
notepad = ['notepad', 'text pad', 'text editor', 'text writer', 'text page']
player = ['media', 'player', 'video', 'window', 'vlc']


while True:
    ts.speak('you have to write the task')
    print("enter ur action:", end="")
    texts = input()

    if (initiate[0] in texts) or (initiate[1] in texts) or (initiate[2] in texts) or (initiate[3] in texts) or (initiate[4] in texts) or (initiate[5] in texts):

        if (notepad[0] in texts) or (notepad[1] in texts) or (notepad[2] in texts) or (notepad[3] in texts) or (notepad[4] in texts):
            ts.speak('opening notepad')
            os.system(
                'notepad')
        elif (browser[0] in texts) or (browser[1] in texts) or (browser[2] in texts) or (browser[3] in texts) or (browser[4] in texts):
            ts.speak('opening chrome browser')
            os.system(
                'C:\Program Files (x86)\Google\Chrome\Application\chrome')
        elif (player[1] in texts) or (player[2] in texts):
            if (player[0] in texts or player[3] in texts):
                ts.speak('opening window media player')
                os.system('wmplayer')
            if (player[4] in texts):
                ts.speak('opening vlc player')
                os.system('vlc')
            else:
                ts.speak("player does't exits")
        elif (terminate[0] in texts) or (terminate[1] in texts) or (terminate[2] in texts) or (terminate[3] in texts) or (terminate[4] in texts) or (terminate[5] in texts):
            ts.speak('see you again, have a nice day')
            break
        else:
            ts.speak('not found')

    elif (terminate[0] in texts) or (terminate[1] in texts) or (terminate[2] in texts) or (terminate[3] in texts) or (terminate[4] in texts) or (terminate[5] in texts):
        ts.speak('see you again, have a nice day')
        break
    else:
        ts.speak('currently these services not supporting')
        print('Not supporting')