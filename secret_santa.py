#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Instructions:
# Create input.txt with names of participants on every string. (use UTF-8 encoding, please)
# Edit message template for your own purposes.
# Run script and send everyone their personal messages generated in Secret Santa folder.
# Merry Christmas, folks!
import os
import random
resultDirName = 'Secret Santa'
#msgTemplate = "Your custom message template. First argument is the presenter name. Second one - doney's name."
msgTemplate = "С наступающим тебя, %s!\n%s с нетерпением ждёт твоего незабываемого подарка, постарайся сделать его особенным :)\nУвидимся в эту пятницу в 11:30 в холле ИКСа. Там ты сможешь подарить свой подарок и встретить своего Тайного Санту.\nС уважением,\nНовогодний креатив от АС-132"
presenters = open("input.txt").read().splitlines()
doneys = list(presenters)
pairs = {}
while len(presenters) > 0:
    doneyIdx = random.randint(0, len(doneys) - 1)
    while presenters[0] == doneys[doneyIdx]:
        doneyIdx = random.randint(0, len(doneys) - 1)
    pairs[presenters[0]] = doneys[doneyIdx]
    del presenters[0]
    del doneys[doneyIdx]
if not os.path.exists(resultDirName):
    os.makedirs(resultDirName)
for pair in pairs:
    file = open("%s/%s.txt" % (resultDirName, pairs[pair].decode('utf-8')), "w")
    file.write(msgTemplate % (pairs[pair], pair))