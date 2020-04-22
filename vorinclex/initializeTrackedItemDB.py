#OPENS THE REGION ACTIVE MARKET ITEMS LIST AND OPENS THE TYPEID:ITEMNAME LIST AND CONNECTS THE NAME OF EACH ACTIVE ITEM TO ITS ID, THEN PUTS THE RESULT IN ACTIVEITEMS.JSON
import json, time

import mktconfig

from util import uniLog

mktset = {}


itemrefdat = {}
#load itemref data from file into dictionary
with open(mktconfig.typeidref, "r") as typeidjsonfile:
	itemrefdat = json.load(typeidjsonfile)
	typeidjsonfile.close()

#open scrape data into dictionary
with open(mktconfig.scrapeoutput, "r") as scrape:
	jscrape = json.load(scrape)
	scrape.close()




#for each market item in the scrape, find its name
mktset.update({jscrape['response'][0] : itemrefdat[str(jscrape['response'][0])]})

print('starting loop')
uniLog('Collating...')

numProds = len(jscrape['response'])
for i in range(0,numProds):
	try:
		mktset.update({jscrape['response'][i] : {'ItemName' : itemrefdat[str(jscrape['response'][i])], 'ItemID' : jscrape['response'][i] }})
		mktset[jscrape['response'][i]].update({'VolOnMkt' : 0})
		mktset[jscrape['response'][i]].update({'DaysSupplyRemaining' : 0})
		mktset[jscrape['response'][i]].update({'SellPrices' : []})
		mktset[jscrape['response'][i]].update({'Competitors' : []})
		mktset[jscrape['response'][i]].update({'DailyISKFlux' : 0})
		mktset[jscrape['response'][i]].update({'DailyVol' : 0})


		print(itemrefdat[str(jscrape['response'][i])])
		print(jscrape['response'][i])
	except KeyError:
		uniLog('updateItems.py KeyError on key '+str(jscrape['response'][i]))
		continue
	except:
		uniLog('updateItems.py unknown error on key '+str(jscrape['response'][i]))
		continue

uniLog('Collation of items to IDs complete. marketSet dictionary updated.')
print('complete')

#Record in file
with open(mktconfig.activeitems, 'w') as activeitemsfile:
	activeitemsfile.write(json.dumps(mktset))

uniLog('Active items written to file '+ mktconfig.activeitems)
print('Active items written to file '+ mktconfig.activeitems)

time.sleep(30)

