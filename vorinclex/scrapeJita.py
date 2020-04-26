#OPENS activeItemsVol.json AND:
#FOR EACH ITEM WITH SIGNIFICANT ISKFLUX, SCRAPES JITA BUY COST TO A FILE IN /jitaOrders directory

import json, time
from datetime import datetime

import mktconfig

from util import uniLog
from wrapper import callESIorders, compileESIregionOrders

print('STARTING scrapeJita.py')
uniLog('STARTING scrapeJita.py')


#Load active items
with open(mktconfig.activeItemsVol, 'r') as activeitemsfile:
	activeitems = json.load(activeitemsfile)

#Iterate through items
items = activeitems.keys()


for g in items:
	print(str(g))
	workingItem = g
	workingItemID = str(activeitems[str(workingItem)]['ItemID'])

	#DONT WASTE TIME FETCHING MARGIN DATA ON WORTHLESS MARKET ITEMS
	if activeitems[workingItem]['DailyISKFlux'] < mktconfig.minMkt:
		continue
	try:
		response = compileESIregionOrders(mktconfig.sourceRegion, 'sell', 1, str(activeitems[str(workingItem)]['ItemID']))
		with open('jitaOrders\\JitaSellOrders'+workingItemID+'.json','w') as JBVfile:
				JBVfile.write(json.dumps(response))
	except:
		uniLog('ERROR: UNABLE TO WRITE JITA ORDERS FOR '+str(workingItemID))
		
	print(json.dumps(response))

print('COMPLETED scrapeJita.py')
uniLog('COMPLETED scrapeJita.py')

time.sleep(200)
exit()