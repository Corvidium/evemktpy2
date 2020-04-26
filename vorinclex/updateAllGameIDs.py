#FROM A LIST OF ALL GAME IDS, CREATES THE SAME LIST IN JSON FORMAT
import json, time

import mktconfig

itemref = {}

#build  itemref dictionary from raw text
with open(mktconfig.typeidsrc, "r", encoding="utf8") as typereffile:
	line = typereffile.readline()
	#line2 = typereffile.readline()
	cnt = 0
	while line:
		x = line.split(',', 1)
		try:
			#BUILD ITEMREF DICTIONARY OF ITEMID:ITEMNAME ASSOCIATION
			itemref.update({x[0]:x[1].strip()})
			print(str(cnt)+':::' +x[0]+x[1])
			line = typereffile.readline()
			cnt += 1
		except:
			print('break on iteration '+str(cnt))
			break

#put reference dictionary into a JSON file
with open(mktconfig.typeidref, 'w') as activeidfile:
	activeidfile.write(json.dumps(itemref))



print('typeids updated')
time.sleep(10)
