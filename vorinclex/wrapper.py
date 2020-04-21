
import requests, json, datetime, mktconfig
#from collections import OrderedDict


def mkLog(some_data):
	with open(mktconfig.scrapelog, "a") as file:
		file.write('\n')
		file.write('['+str(datetime.datetime.now())+'] ')
		file.write(str(type(some_data)))
		if(type(some_data) == str):
			file.write(some_data)
		file.close()
	return 1

#Return a list of historical market statistics for the specified type in a region
def callESIhistory(region_id, type_id):
	
	headers = {
    'accept': 'application/json',
	}
	params = (
	    ('datasource', 'tranquility'),
	)

	queryString = mktconfig.esiurl + '/latest/markets/' + str(region_id) + '/history/?datasource=tranquility&type_id=' + str(type_id)
	print(queryString)

	response = requests.get(queryString, headers=headers)

	return response

#Return a list of orders in a region
def callESIorders(region_id, order_type = 'all', page = 1, type_id = 'unsupplied'):
	headers = {
    'accept': 'application/json',
	}
	params = (
		('datasource', 'tranquility'),
		('page', str(page)),
	)

	queryString = mktconfig.esiurl + '/latest/markets/' + str(region_id) + '/orders/?datasource=tranquility&order_type=' + str(order_type) + '&page=' + str(page) 
	if type_id != 'unsupplied':
		queryString += '&type_id=' + str(type_id)
	print(queryString)


	response = requests.get(queryString, headers=headers, params=params)

	return response

#Return a list of type IDs that have active orders in the region, for efficient market indexing.
def callESItypes(region_id, page = 1):
	
	headers = {
    'accept': 'application/json',
	}
	params = (
	    ('datasource', 'tranquility'),
	    ('page', str(page)),
	)

	queryString = mktconfig.esiurl + '/latest/markets/' + str(region_id) + '/types/?datasource=tranquility&page=' + str(page)
	print(queryString)
	mkLog(queryString)
	

	#response = requests.get(queryString, headers=headers, params=params)
	response = requests.get(queryString)
	#mkLog(response.text)

	return response


def compileESItypes(region_id):
	i = 2
	
	prima = callESItypes(region_id, 1)
	compoundTypes = prima.json()

	mkLog(compoundTypes)

	pages = int(prima.headers['X-Pages'])

	if ( pages > 1):
		for x in range (0, pages):
			response2 = callESItypes(region_id, i)
			
			compoundTypes.extend(response2.json())
			i = i + 1

	
	responseDict = {
	    'time':str(datetime.datetime.now()),
	    'headers': dict(prima.headers),
	    'response': compoundTypes
	}
	mkLog(responseDict)

	return responseDict

def responseArchive(response):

	responseDict = {
	    'time':str(datetime.datetime.now()),
	    'headers': dict(response.headers),
	    'response': response.json()
	}

	with open(mktconfig.scrapeoutput, "w") as file:
		file.write(json.dumps(responseDict))
		file.close()

	return 1

def logArchive(dict):

	with open(mktconfig.scrapeoutput, "w") as file:
		file.write(json.dumps(dict))

	return 1

#Return a list of orders from the structure
def callESIstructureOrders(structure_id, page = 1):
	
	
	queryString = mktconfig.esiurl+'/latest/markets/structures/'+str(mktconfig.destoStruct)+'/?datasource=tranquility&page='+str(page)+'&token='+str(mktconfig.token)
	print(queryString)
	mkLog(queryString)
	
	response = requests.get(queryString)

	
	return response

#build a complete list of market orders in a structure. Necessary to compute current on-market volume (only in destination system - Esoteria) (note: this is inefficient in Jita; don't use) and to get current lowest sell price in Jita containing at least that volume
def compileESIstructureOrders(structure_id):
	i = 2
	
	prima = callESIstructureOrders(structure_id, 1)
	compoundOrders = prima.json()
	try:

		pages = int(prima.headers['x-pages'])
	except:
		print('response.text is: ')
		print(prima.text)
		mkLog(prima.text)


	if ( pages > 1):
		for x in range (0, pages):
			response2 = callESIstructureOrders(structure_id, i)
			
			compoundOrders.extend(response2.json())
			print('PAGE '+str(i)+' of '+ str(pages))
			i = i + 1

	
	responseDict = {
	    'time':str(datetime.datetime.now()),
	    'headers': dict(prima.headers),
	    'response': compoundOrders
	}
	mkLog(responseDict)

	return responseDict
