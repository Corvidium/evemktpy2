#package import
import requests, json, datetime, time

#config import
import mktconfig


print(mktconfig.esiurl)

#from collections import OrderedDict
from wrapper import mkLog, callESIorders, callESIhistory, callESItypes, compileESItypes, responseArchive, logArchive


print("updateMarketItems.py EXECUTION INITIATED\n")
mkLog("updateMarketItems.py EXECUTION INITIATED")

responseData = compileESItypes(mktconfig.destoRegion) #esoteria region 10000039

logArchive(responseData)


print("updateMarketItems.py EXECUTION COMPLETE")
mkLog("updateMarketItems.py EXECUTION COMPLETE")


