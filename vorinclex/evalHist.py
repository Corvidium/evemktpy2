import json, time, datetime
import mktconfig
from util import uniLog

#Load active items
with open(mktconfig.activeitems, 'r') as activeitemsfile:
	activeitems = json.load(activeitemsfile)

#Iterate through items
items = activeitems.keys()
ranklist = []

for g in items:
	print(str(g))

	workingitem = g
	#open scrape data into dictionary
	try:
		with open('hist/'+str(workingitem)+'hist.json', "r") as hist:
			mkthist = json.load(hist)
	except:
		uniLog("Error in evalHist.py opening file "+str(workingitem)+'hist.json for item '+activeitems[str(workingitem)]['ItemName'])
		continue

	#print(json.dumps(mkthist))
	try:
		startdate = mkthist[0]['date'].split()
		vol = [x['volume'] for x in mkthist]
		price = [x['average'] for x in mkthist]
	except:
		continue
	#print(str(price[0]))

	totvol = 0
	h = 0
	for i in vol:
		#print(vol[h])
		totvol+=vol[h]
		h+=1

	totprice = float()
	h = 0
	for j in price:
		#print(price[h])
		totprice+=price[h]
		h+=1
	try:
		avprice = totprice/h
	except:
		avprice = 0

	#print('sum is '+str(totvol))



	#print(str(startdate[0]))

	datearr = startdate[0].split('-')

	#print(datetime.datetime.now())
	#print('complete')

	curY = int(datetime.datetime.today().year)
	curM = int(datetime.datetime.today().month)
	curD = int(datetime.datetime.today().day)

	elapsedY = curY-int(datearr[0])
	elapsedM = curM-int(datearr[1])
	elapsedD = curD-int(datearr[2])

	totdays = 365*(elapsedY)+30.4375*(elapsedM)+(elapsedD)
	dailyISKflux = avprice*totvol/totdays
	avgVol = totvol/totdays

	#print('days covered: '+str(totdays)+' including volume of '+str(totvol)+ ' averaging to '+str(totvol/totdays)+' units per day at average price '+str(avprice)+' for daily ISK volume of '+str(dailyISKflux)+' ISK per day sold of this item')
	displayflux = '{flux: ,.0f}'.format(flux = dailyISKflux)

	#UPDATE ACTIVEITEMS LIST WITH VOLUME
	activeitems[str(workingitem)]['DailyISKFlux']=dailyISKflux
	activeitems[str(workingitem)]['DailyVol']=avgVol


	#Create array with daily isk volume as first index item, for easy sorting
	ranklist.append([dailyISKflux,workingitem,activeitems[str(workingitem)]['ItemName'],avgVol])
	

	#print(json.dumps(activeitems[str(workingitem)]))


ranklist.sort()
ranklist.reverse()

i = 0
while i in range(0,50):
	j = 0
	print(json.dumps(activeitems[str(ranklist[i][1])]))
	while j in range(0,4):
		print(str(ranklist[i][j]))
		j+=1
	print('-----------------------------------------------')
	i+=1
	
with open(mktconfig.activeItemsVol, "w") as file:
		file.write(json.dumps(activeitems))

print("WRITTEN TO FILE "+mktconfig.activeItemsVol)


#print(json.dumps(activeitems))
time.sleep(300)