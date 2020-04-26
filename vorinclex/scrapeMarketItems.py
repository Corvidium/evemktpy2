#CALLS API TO GET LIST OF ALL GAMEIDS WITH MARKET HISTORY IN TARGET REGION AND PUTS IT IN activeTypesScrape.json

#package import
import requests, json, datetime, time

#config import
import mktconfig

print(mktconfig.esiurl)

#from collections import OrderedDict
from wrapper import mkLog, callESIorders, callESIhistory, callESItypes, compileESItypes, responseArchive, logArchive


print("scrapeMarketItems.py EXECUTION INITIATED\n")
mkLog("scrapeMarketItems.py EXECUTION INITIATED")

responseData = compileESItypes(mktconfig.destoRegion) #esoteria region 10000039
logArchive(responseData)

print("scrapeMarketItems.py EXECUTION COMPLETE")
mkLog("scrapeMarketItems.py EXECUTION COMPLETE")

time.sleep(30)
exit()
