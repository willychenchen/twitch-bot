#!/usr/bin/env python

from sys import argv
from src.bot import *
from src.config.config import *
import threading

#config['username']='kappawatch'
#config['oauth_password']='oauth:xcdmitpw9piflod2e8glqzp423md2o'
#bot = Roboraj(config).run()


userFile = open('users.txt', 'r').read()
userSplit = userFile.split(chr(10))

for user in userSplit:
    userData = user.split(':')
    config['username'] = userData[0]
    config['oauth_password'] = 'oauth:%s' % userData[1]
    
    
    twitchThread = threading.Thread(target=Roboraj(config).run)
    twitchThread.start()
