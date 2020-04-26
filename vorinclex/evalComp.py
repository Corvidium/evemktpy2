#OPENS activeItemsVol.json
#OPENS STRUCTURE ORDERS
#FOR EACH ORDER, IDENTIFY ITS ITEM, THEN COMPILE WITH THE ITEM RECORD THIS COMPETITOR SELL ORDER TIMESTAMP, THIS PRICE, AND THIS VOLUME OFFERED FOR SALE

#IF ANY SELL ORDERS ARE FOR AN UNFAMILIAR ITEM, TRY TO REPAIR THE ORIGINAL activeitems.json SO USER CAN RESTART ALL SCRIPTS

#FOR EACH ITEM, EVALUATE: 
#    1) WHETHER STOCK ON MARKET WILL RUN OUT SOON AT HISTORICAL VOLUMES (I.E. FIND IMPENDING SHORTAGES)
#    2) HOW MUCH MARGIN A CURRENT SELLER RECEIVES GIVEN CURRENT COMPETITION (I.E. FIND HIGH MARGIN LOW COMPETITION ITEMS)



import json, time
from datetime import datetime

import mktconfig

from util import uniLog
from wrapper import callESIhistory



with open(mktconfig.structureOutput+str(mktconfig.destoStruct)+'.json', "r") as ordersjsonfile:
	ordersKS = json.load(ordersjsonfile)

with open(mktconfig.activeItemsVol, "r") as activeitemsfile:
	activeitems = json.load(activeitemsfile)


#ESTABLISH REFERENCE TIME WHEN MARKET WAS POLLED
snapshotT = ordersKS['headers']['Date'][3:]
snapshotTime = datetime.strptime(snapshotT,", %d %b %Y %H:%M:%S GMT")
print('time is')
print(snapshotTime)


#record items for which history is missing
holes = []
#DERIVE STOCK ON MARKET SELL ORDERS FROM KEEPSTAR ORDER LIST
for i in ordersKS['response']:
	if i['is_buy_order'] == True:
		continue
	issueT = i['issued'].strip('Z').replace('T',' ')
	issueTime = datetime.strptime(i['issued'].strip('Z').replace('T',' '), "%Y-%m-%d %H:%M:%S")
	#print(issueTime)
	timeSinceUpdated = snapshotTime-issueTime
	#print(timeSinceUpdated)
	#print(timeSinceUpdated.total_seconds())
	#IDENTIFY BRACKETS OF COMPETITION INTENSITY AT 1H, 6H, 24H, AND 7D

	try:
		activeitems[str(i['type_id'])]['VolOnMkt']+=i['volume_remain']
		activeitems[str(i['type_id'])]['Competitors'].append([timeSinceUpdated.total_seconds(),i['volume_remain'],str(timeSinceUpdated),str(issueT)])
		activeitems[str(i['type_id'])]['SellPrices'].append([i['price'],timeSinceUpdated.total_seconds(),i['volume_remain']])
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
outOfStock = {}
oneStock = {}
threeStock = {}

ranklist=[]
#outList = []
#lowList = []
anyItems = {}

#Compute newly available indices - days of supply on market, NUMBER OF COMPETITORS ACTIVE IN ONE DAY, MARGIN PER UNIT SOLD, 
for i in activeitems:
	print(json.dumps(i))

	activeitems[i]['Competitors'].sort()
	activeitems[i]['SellPrices'].sort()

	#EVALUATE FREQUENCY OF COMPETITOR UPDATES TO MARKET ORDERS
	if len(activeitems[i]['Competitors'])>0:
		mostRecentUpdate = activeitems[i]['Competitors'][0][0]
		myShare = min(mostRecentUpdate/86400/mktconfig.daysTillAFK,1)
		#print('myShare '+str(myShare))
		esoPrice = activeitems[i]['SellPrices'][0][0]
		JBV = activeitems[i]['JitaBuyValue']
		dailyVol = activeitems[i]['DailyVol']

		#TAXATION FACTORED IN
		perUnitProfit = (esoPrice-JBV-esoPrice*(mktconfig.brokersFee+mktconfig.salesTax+mktconfig.transportFee))

		myFlux = myShare*activeitems[i]['DailyISKFlux']
		dailyProfit = dailyVol * perUnitProfit
		myDailyProfit = dailyProfit*myShare

		activeitems[i]['myMktShare'] = myShare
		activeitems[i]['myDailyISKFlux'] = myFlux
		activeitems[i]['myDailyISKMargin'] = myDailyProfit
		activeitems[i]['PerUnitMargin'] = perUnitProfit
	



	#COMPUTE DAYS SUPPLY REMAINING
	if activeitems[i]['DailyVol'] == 0:
		continue

	try:
		activeitems[i]['DaysSupplyRemaining'] = activeitems[i]['VolOnMkt']/activeitems[i]['DailyVol']
		
		if activeitems[i]['DaysSupplyRemaining'] == 0:
			outOfStock.update({i:activeitems[i]})
			#outList.append([activeitems[i]['DailyISKFlux'],activeitems[i]['ItemID'],activeitems[i]['ItemName']])
		elif activeitems[i]['DaysSupplyRemaining'] < 1:
			oneStock.update({i:activeitems[i]})
			#oneList.append([activeitems[i]['DailyISKFlux'],activeitems[i]['ItemID'],activeitems[i]['ItemName']])
		elif activeitems[i]['DaysSupplyRemaining'] < 3:
			threeStock.update({i:activeitems[i]})
			#lowList.append([activeitems[i]['DailyISKFlux'],activeitems[i]['ItemID'],activeitems[i]['ItemName']])
		#ranklist.append([activeitems[i]['DaysSupplyRemaining'],activeitems[i]['ItemName'],activeitems[i]['ItemID'],activeitems[i]['DailyISKFlux']])
		#print(str(i['volume_remain']))
	except KeyError:
		uniLog('KeyError in evalComp.py on itemID '+str(activeitems[i]['ItemID'])+' for itemName '+str(activeitems[i]['ItemName']))
	except:
		uniLog('Unknown Error in evalComp.py on itemID '+str(activeitems[i]['ItemID'])+' for itemName '+str(activeitems[i]['ItemName']))
		uniLog('Possibly no item history.')

	anyItems.update({str(i):activeitems[i]})
	print(json.dumps(activeitems[i]))
	print(json.dumps(anyItems[i]))
	if len(anyItems[i]['Competitors'])>0:
		anyItems[i]['Competitors'] = activeitems[i]['Competitors'][0]
	if len(anyItems[i]['SellPrices'])>0:
		anyItems[i]['SellPrices'] = activeitems[i]['SellPrices'][0]



#print(json.dumps(activeitems))
with open(mktconfig.activeItemsComp, "w") as file:
		file.write(json.dumps(activeitems))

print("WRITTEN TO FILE "+mktconfig.activeItemsComp)


alch = sorted(outOfStock.items(),key=lambda item:1/item[1]['DailyISKFlux'])
alch2 = sorted(oneStock.items(),key=lambda item:1/item[1]['DailyISKFlux'])
alch3 = sorted(threeStock.items(),key=lambda item:1/item[1]['DailyISKFlux'])
alchG = sorted(anyItems.items(),key=lambda item:item[1]['myDailyISKMargin']*(-1))

with open('maxProfitOutStock.json','w') as profitfile:
	profitfile.write(json.dumps(alch))
print('alch written')
with open('maxProfitOneStock.json','w') as profitfile2:
	profitfile2.write(json.dumps(alch2))
print('alch2 written')
with open('maxProfitThreeStock.json','w') as profitfile3:
	profitfile3.write(json.dumps(alch3))
print('alch3 written')
with open('maxProfitAnyStock.json','w') as profitfile4:
	profitfile4.write(json.dumps(alchG))
print('alchG written')


time.sleep(300)