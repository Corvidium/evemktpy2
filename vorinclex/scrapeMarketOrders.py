import requests,json,time,datetime,subprocess, os
import mktconfig

from wrapper import compileESIstructureOrders, callESIstructureOrders,mkLog


print("EXECUTION INITIATED\n")
mkLog("EXECUTION INITIATED")




responseData = compileESIstructureOrders(mktconfig.destoStruct) #esoteria region 10000039

with open(mktconfig.structureOutput+mktconfig.destoStruct+'.json', "w") as file:
		file.write(json.dumps(responseData))

print("EXECUTION COMPLETE")
mkLog("EXECUTION COMPLETE")
time.sleep(30)