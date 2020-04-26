#LOADS ACTIVEITEMS, THEN SCRAPES TARGET REGION'S DAILY VOLUME AND PRICE HISTORY FOR EACH ITEM TO THE hist/ DIRECTORY

import time, json, datetime, os.path
import mktconfig
from util import uniLog
from wrapper import callESIhistory



#load itemref data from file into dictionary
with open(mktconfig.activeitems, "r") as activeitemsfile:
	activeitems = json.load(activeitemsfile)

#Record one year of market history to file for every active item in market - WARNING: LONG RUNNING ~50 MINUTES
i = 0
for key in activeitems:
	
	try:
		hist = callESIhistory(mktconfig.destoRegion, key)
		jhist = hist.json()
		#print(json.dumps(jhist))
		with open('hist\\'+str(key)+'hist.json','w') as histfile:
			histfile.write(json.dumps(jhist))
	except:
		uniLog('updateHist.py error on '+str(key))


print('EXECUTION COMPLETE - updateHist.py')
time.sleep(30)


