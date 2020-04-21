#package import
import requests, json, datetime, time

#config import
import mktconfig

#utilities import (logging etc)
#from util import mklog

print(mktconfig.esiurl)



#from collections import OrderedDict
from wrapper import mkLog, callESIorders, callESIhistory, callESItypes, compileESItypes, responseArchive, logArchive


print("EXECUTION INITIATED\n")
mkLog("EXECUTION INITIATED")
#time.sleep(1)
time.sleep(1)

#responseData = callESItypes(10000039, 1)

#responseData = callESIhistory(10000039, 25624)

#responseData = callESIorders(10000039,'all',1)


responseData = compileESItypes(mktconfig.destoRegion) #esoteria region 10000039

logArchive(responseData)

	
#responseArchive(responseData)



print("EXECUTION COMPLETE")
mkLog("EXECUTION COMPLETE")


