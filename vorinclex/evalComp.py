import json, time

import mktconfig

from util import uniLog
from wrapper import callESIhistory



with open('structureOrdersOut1024004680659.json', "r") as ordersjsonfile:
	ordersKS = json.load(ordersjsonfile)

with open('activeItemsVol.json', "r") as activeitemsfile:
	activeitems = json.load(activeitemsfile)

#record items for which history is missing
holes = []
#DERIVE STOCK ON MARKET SELL ORDERS FROM KEEPSTAR ORDER LIST
for i in ordersKS['response']:
	if i['is_buy_order'] == True:
		continue

	try:
		activeitems[str(i['type_id'])]['VolOnMkt']+=i['volume_remain']
		#print(str(i['volume_remain']))
	except KeyError:
		#Usually caused by having no 'volonmarket' parameter due to failure to index by history.py, and then failure to create by itemproc.py
		uniLog('KeyError in evalComp.py finding active item '+str(i['type_id']))
		holes.append(i['type_id'])
	except:
		uniLog('Unknown Error in evalComp.py on item '+str(i['type_id']))


#REMOVE DUPLICATES
holesl = dict.fromkeys(holes)
holes = list(holesl)

if len(holes)>0:
	print('HOLES IN HISTORY')
	print(holes)
	uniLog('HOLES IN HISTORY - NON INDEXED ITEMS')
	uniLog(str(holes))
	#MANUAL SWITCH FOR ADDING NON-INDEXED ITEMS TO SCRAPEOUTPUT TO RE-RUN initializeTrackedItemDB.py
	if False:
		with open('scrapeoutput.json','r')as primalitemsfile:
			primalitems = json.load(primalitemsfile)

		for i in holes:
			print('WRITING TO scrapeoutput.JSON '+str(i))
			uniLog('WRITING TO scrapeoutput.JSON '+str(i))
			primalitems['response'].append(i)

		with open('scrapeoutput.json','w')as primalitemsfile:
			primalitemsfile.write(json.dumps(primalitems))

	#MANUAL SWITCH FOR FILLING HOLES IN HISTORY
	if False:
		uniLog('evalComp.py fixing holes in history')
		for i in holes:
			print('Fixing hole '+str(i))
			uniLog('Fixing hole '+str(i))
			key = i
			hist = callESIhistory(mktconfig.destoRegion, key)
			jhist = hist.json()
			#print(json.dumps(jhist))

			with open(str(key)+'hist.json','w') as histfile:
				histfile.write(json.dumps(jhist))
		print('Done fixing holes')
		uniLog('Done fixing holes')

#INITIALIZE TARGET VARIABLES
lowStock = {}
outOfStock = {}
ranklist=[]
outList = []
lowList = []


#Compute newly available indices - days of supply on market
for i in activeitems:
	print(json.dumps(i))
	if activeitems[i]['DailyVol'] == 0:
		continue
	try:
		activeitems[i]['DaysSupplyRemaining'] = activeitems[i]['VolOnMkt']/activeitems[i]['DailyVol']
		
		if activeitems[i]['DaysSupplyRemaining'] == 0:
			outOfStock.update({i:activeitems[i]})
			outList.append([activeitems[i]['DailyISKFlux'],activeitems[i]['ItemID'],activeitems[i]['ItemName']])
		else if activeitems[i]['DaysSupplyRemaining'] < 3:
			lowStock.update({i:activeitems[i]})
			lowList.append([activeitems[i]['DailyISKFlux'],activeitems[i]['ItemID'],activeitems[i]['ItemName']])
		ranklist.append([activeitems[i]['DaysSupplyRemaining'],activeitems[i]['ItemName'],activeitems[i]['ItemID'],activeitems[i]['DailyISKFlux']])
		#print(str(i['volume_remain']))
	except KeyError:
		uniLog('KeyError in evalComp.py on itemID '+str(activeitems[i]['ItemID'])+' for itemName '+str(activeitems[i]['ItemName']))
	except:
		uniLog('Unknown Error in evalComp.py on itemID '+str(activeitems[i]['ItemID'])+' for itemName '+str(activeitems[i]['ItemName']))
		uniLog('Possibly no item history.')
	



print(json.dumps(activeitems))
with open(mktconfig.activeItemsComp, "w") as file:
		file.write(json.dumps(activeitems))

print("WRITTEN TO FILE "+mktconfig.activeItemsComp)


alch = sorted(outOfStock.items(),key=lambda item:1/item[1]['DailyISKFlux'])
alch2 = sorted(lowStock.items(),key=lambda item:1/item[1]['DailyISKFlux'])

with open('maxProfitOutStock.json','w') as profitfile:
	profitfile.write(json.dumps(alch))
print('alch written')
with open('maxProfitLowStock.json','w') as profitfile2:
	profitfile2.write(json.dumps(alch2))
print('alch2 written')

time.sleep(30)


print({k: v for k, v in sorted(outOfStock.items(), key=lambda item: item['DailyISKFlux'])})
time.sleep(10)
#FIND ALL OUT OF STOCK ITEMS
lowList.sort()
outList.sort()

outOfStockList = list(outOfStock)
print(outOfStockList)
print(json.dumps(outOfStock))
if 0:
	ranklist.sort()
	i = 0
	while i in range(0,50):
		j = 0
		print(json.dumps(activeitems[str(ranklist[i][2])]))
		while j in range(0,4):
			print(str(ranklist[i][j]))
			j+=1
		print('-----------------------------------------------')
		i+=1




time.sleep(300)