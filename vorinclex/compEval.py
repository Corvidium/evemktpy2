import json, time

import mktconfig

from util import uniLog




with open('structureOrdersOut1024004680659.json', "r") as ordersjsonfile:
	ordersKS = json.load(ordersjsonfile)

with open('activeItemsVol.json', "r") as activeitemsfile:
	activeitems = json.load(activeitemsfile)

for i in ordersKS['response']:
	if i['is_buy_order'] = True:
		continue
	print('.')

	activeitems[i['type_id']]['VolOnMkt']+=i['volume_remain']

print(json.dumps(activeitems))

time.sleep(300)