# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import re
from datetime import datetime, timedelta
import time

text="What happens to the energy added to or removed from an object (that is really made up of many particles bound together by internal e.g. molecular forces) by things like my non-conservative handas I give a block treated as a particle a push, or non-conservative kinetic friction and drag forces as they act on the block to slow it down as it slides along a table? This is not a trivial question. To properly answer it we have to descend all the way into the conceptual abyss of treating every single particle that makes up the system we call the block and every single particle that makes up the system consisting of everything else in the Universe but the block and all of the internal forces between them  which happen, as far as we can tell, to be strictly conservative forces  and then somehow average over them to recover the ability to treat the block like a particle, the table like a fixed, immovable object it slides on, and friction like a comparatively simple force that does non-conservative work on the block. It requires us to invent things like statistical mechanics to do the averaging, thermodynamics to describe certain kinds of averaged systems, and whole new sciences such as chemistry and biology that use averaged energy concepts with their own fairly stable rules that cannot easily be connected back to the microscopic interactions that bind quarks and electrons into atoms and atoms together into molecules. It’s easy to get lost in this, because it is both fascinating and really difficult. I’m therefore going to give you a very important empirical law (that we can understand well enough from our treatment of particles so far) and a rather heuristic description of the connections between microscopic interactions and energy and the macroscopic mechanical energy of things like blocks, or cars, or human bodies. The important empirical law is the Law of Conservation of Energy86. Whenever we examine a physical system and try very hard to keep track of all of the mechanical energy exchanges withing that system and between the system and its surroundings, we find that we can always account for them all without any gain or loss. In other words, we find that the total mechanical energy of an isolated system never changes, and if we add or remove mechanical energy to/from the system, it has to come from or go to somewhere outside of the system. This result, applied to well defined systems of particles, can be formulated as the First Law of Thermodynamics: Qin = Eof +Wby (325) In words, the heat energy flowing in to a system equals the change in the internal total mechanical energy of the system plus the external work (if any) done by the system on its surroundings. The total mechanical energy of the system itself is just the sum of the potential and kinetic energies of all of its internal parts and is simple enough to understand if not to compute. The work done by the system on its surroundings is similarly simple enough to understand if not to compute. The hard part of this law is the definition of heat energy, and sadly, I’m not going to give you. So take the following with a grain of salt, so to speak. When a block slides down a rough table from some initial velocity to rest, kinetic friction turns the bulk organized kinetic energy of the collectively moving mass into disorganized microscopic energy  heat. As the rough microscopic surfaces bounce off of one another and form and break chemical bonds, it sets the actual molecules of the block bounding, increasing the internal microscopic mechanical energy of the block and warming it up. Some of it similarly increasing the internal microscopic mechanical energy of the table it slide across, warming it up. The Homework over energy is due thursday at 11PM. Some of it appears as light energy (electromagnetic radiation) or sound energy initially organized energy forms that themselves become ever more disorganized. So There will be homework over Section 4 due next monday. Eventually, the initial organized energy of the block becomes a tiny increase in the average internal mechanical energy of a very, very large number of objects both inside and outside of the original system that we call the block, a process we call being awesome."

words = text.split()

browser = webdriver.Firefox()
wait = WebDriverWait(browser, 10)
browser.get('http://30d2342e.ngrok.io/')

location1=wait.until(EC.presence_of_element_located((By.ID, "chat-input")))
while True:
    i=0
    for items in words:
        i+=i

        if i==20:
            time.sleep(5)
            location1.send_keys("@test2016-08-05T03:00:00.000ZTrain with Josh on August 25th at Fitworks at 9:00 PM")
            time.sleep(2)
        location1.send_keys(" "+items+" ")
        location1.send_keys(Keys.ENTER)
        time.sleep(2)
