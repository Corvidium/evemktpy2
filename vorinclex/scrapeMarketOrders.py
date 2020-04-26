#SCRAPES ALL SELL ORDERS IN TARGET STRUCTURE

import requests,json,time,datetime,subprocess, os
import mktconfig

from wrapper import compileESIstructureOrders, callESIstructureOrders,mkLog


print("EXECUTION INITIATED\n")
mkLog("EXECUTION INITIATED")



try:
	responseData = compileESIstructureOrders(mktconfig.destoStruct) #esoteria region 10000039
except:
	print('Failed to update structure orders. Sometimes caused by invalid ESI token - put a new one into mktconfig.py by getting it from https://esi.evetech.net/ui/#/Market/get_markets_structures_structure_id')
	mkLog('Failed to update structure orders. Sometimes caused by invalid ESI token - put a new one into mktconfig.py by getting it from https://esi.evetech.net/ui/#/Market/get_markets_structures_structure_id')
	time.sleep(300)
	exit()
with open(mktconfig.structureOutput+mktconfig.destoStruct+'.json', "w") as file:
		file.write(json.dumps(responseData))

print("EXECUTION COMPLETE")
mkLog("EXECUTION COMPLETE")
time.sleep(30)