#OPENS activeItemsVol.json AND:
#FOR EACH ITEM, WRITES THE LOWEST JITA PRICE TO activeItemsVol.json

import json, time
from datetime import datetime

import mktconfig

from util import uniLog
from wrapper import callESIorders, compileESIregionOrders

print('STARTING evalJitaPrice.py')
uniLog('STARTING evalJitaPrice.py')


#Load active items
with open(mktconfig.activeItemsVol, 'r') as activeitemsfile:
	activeitems = json.load(activeitemsfile)

#Iterate through items
items = activeitems.keys()


for g in items:
	print(str(g))
	workingItem = g
	workingItemID = str(activeitems[str(workingItem)]['ItemID'])
	lowPrice = 999999999999


	
	try:
	#OPEN LIST OF THE FORGE ORDERS FOR THIS ITEM
		with open('jitaOrders\\JitaSellOrders'+workingItemID+'.json','r') as JBVfile:
			jitaOrders=json.load(JBVfile)
		uniLog('SUCCESSFULLY OPENED '+'jitaOrders\\JitaSellOrders'+workingItemID+'.json')

		
	#GO THROUGH EACH ORDER TO FIND THE LOWEST PRICE

	
		if(len(jitaOrders['response'])>0):
			lowPrice = jitaOrders['response'][0]['price']
			for h in jitaOrders['response']:
				if (h['price']<lowPrice):
					lowPrice = h['price']
			print('lowPrice is '+str(lowPrice))
			activeitems[str(workingItem)]['JitaBuyValue'] = lowPrice
		
	except:
		uniLog('Error opening '+'jitaOrders\\JitaSellOrders'+workingItemID+'.json')


	
	

with open(mktconfig.activeItemsVol, 'w') as activeitemsfile:
	activeitemsfile.write(json.dumps(activeitems))

print('COMPLETED evalJitaPrice.py')
uniLog('COMPLETED evalJitaPrice.py')

time.sleep(200)
exit()