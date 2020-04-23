#PROCESSES ACTIVEITEMSVOL.JSON TO GET JITA BUY COST OF EACH ITEM WITH SIGNIFICANT DAILY VOLUME IN DESTINATION MARKET

import json, time
from datetime import datetime

import mktconfig

from util import uniLog
from wrapper import callESIorders, compileESIregionOrders

print('starting')
uniLog('starting')


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
	
	response = compileESIregionOrders(mktconfig.sourceRegion, 'sell', 1, str(activeitems[str(workingItem)]['ItemID']))
	with open('jitaOrders\\JitaSellOrders'+workingItemID+'.json','w') as JBVfile:
			JBVfile.write(json.dumps(response))

	print(json.dumps(response))

time.sleep(200)
exit()