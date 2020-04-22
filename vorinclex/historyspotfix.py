import time, json, datetime, os.path
import mktconfig
from util import uniLog
from wrapper import callESIhistory


#for fetching specific item histories
key = 4250
print(key)
hist = callESIhistory(mktconfig.destoRegion, key)
jhist = hist.json()
print(json.dumps(jhist))

with open(str(key)+'hist.json','w') as histfile:
	histfile.write(json.dumps(jhist))




time.sleep(300)


