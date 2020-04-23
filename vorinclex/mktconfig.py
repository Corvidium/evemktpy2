destoRegion = '10000039'
#D-PNP keepstar 1024004680659
destoStruct = '1024004680659'
#Jita 4-4 60003760
sourceStruct = '60003760'
sourceRegion = '10000002'

#API authorization token - REGENERATE token for esi_markets.structure_marketsV1
token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IkpXVC1TaWduYXR1cmUtS2V5IiwidHlwIjoiSldUIn0.eyJzY3AiOiJlc2ktbWFya2V0cy5zdHJ1Y3R1cmVfbWFya2V0cy52MSIsImp0aSI6IjVkNGM4MTMxLTQ0YWItNGIzNy05N2EzLThlNzdiYzMxODljNSIsImtpZCI6IkpXVC1TaWduYXR1cmUtS2V5Iiwic3ViIjoiQ0hBUkFDVEVSOkVWRTo5Njg1ODI5NCIsImF6cCI6IjY4MzA4NGFiNWY4ODQ4ZDRiMTg3NDYyYWMzYjk3Njc3IiwibmFtZSI6IlRpYmVyaXVzIFJob2RlcyIsIm93bmVyIjoiNUdWYzhkZmpIb21ZSEJ3RjhoNkJiYTJqcDBnPSIsImV4cCI6MTU4NzYyNzU1MiwiaXNzIjoibG9naW4uZXZlb25saW5lLmNvbSJ9.O9x4tAKj3SXpScJU9VhBhCaz5cVZimmbw279XZjAZrrYB1R73KtY11Z4kecQj9VgFuiaL3ic0tan_9p3mBatMba8Xf15wZ-s9ZjUg45lM1EI0FR8Ro4v-EWYZAEqnWsG00eN4vTlbX-OWjHDzCWTJX49IpoJ6EfUalmoARyKMkfJ1cBfXFqv-sVUQGZbhJzkSWXNhtemX17ytCf_HBIhFepBO7BKvyn7amjgCjbrxDJlGhN6ZL1P9a0vPRkgSfibPbfRiFq8RcmnZaMW9YLFtDIIGUv0m6Rhio5OoMfANfYwElTFtOJfVyVPsZvc_QxwMdgII6H9DXo1eeSFytQjDA'

#MINIMUM DAILY ISK FLUX TO CONSIDER TRADING IN AN ITEM
minMkt = 1000000
#I'm not gonna wanto to waste time importing something that makes only 50,000ISK but that I have to spend a few seconds a week typing it into market searchbar in jita to buy some volume of it.
apmvalue = 1000000

#Target of API requests
esiurl = 'https://esi.evetech.net'

#Naming convention for storage files
scrapelog = 'scrapelog.txt'
scrapeoutput = 'scrapeoutput.json'
typeidsrc = 'typeid.txt'
typeidref = 'typeids.json'
genlog = 'log.txt'
activeitems = 'activeitems.json'
structureOutput = 'structureOrdersOut'
activeItemsVol = 'activeItemsVol.json'
activeItemsComp = 'activeItemsComp.json'
#number of hours after GMT
timeZone = 8
daysTillAFK = 2

#MARGIN ESTABLISHED IN MONOPOLY CONDITIONS
targetMargin = 0.3
brokersFee = .02
salesTax = .0335
transportFee = .01