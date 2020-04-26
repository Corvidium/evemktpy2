
#Esoteria 10000039
#Wicked Creek 10000006
destoRegion = '10000039'
#D-PNP keepstar 1024004680659
#Deployment C0O6-K keepstar 1032819384255
destoStruct = '1024004680659'


#The Forge 10000002
sourceRegion = '10000002'
#Jita 4-4 60003760
sourceStruct = '60003760'

#API authorization token - REGENERATE token for esi_markets.structure_marketsV1
token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IkpXVC1TaWduYXR1cmUtS2V5IiwidHlwIjoiSldUIn0.eyJzY3AiOiJlc2ktbWFya2V0cy5zdHJ1Y3R1cmVfbWFya2V0cy52MSIsImp0aSI6IjlmNWQ3YzFkLWQyMmMtNGIyYi1iNTQxLTMxYjQ4YzVkNDFkMSIsImtpZCI6IkpXVC1TaWduYXR1cmUtS2V5Iiwic3ViIjoiQ0hBUkFDVEVSOkVWRTo5Njg1ODI5NCIsImF6cCI6IjY4MzA4NGFiNWY4ODQ4ZDRiMTg3NDYyYWMzYjk3Njc3IiwibmFtZSI6IlRpYmVyaXVzIFJob2RlcyIsIm93bmVyIjoiNUdWYzhkZmpIb21ZSEJ3RjhoNkJiYTJqcDBnPSIsImV4cCI6MTU4NzY0ODIzNywiaXNzIjoibG9naW4uZXZlb25saW5lLmNvbSJ9.Y4Ye9rlL2EzrsVb_C8WoR0zE1grYXTMzFA3768z4teh53Cfipls380lgOZT55JB_mzGQLjZOrdTxOXtdWmzCbFoyR7xosjJJWLccW_tl5qQ1nAGsXfau4_CIlcrK6wyUB3omopf5OAb0hXvFrkkzUlcMf6GSbl4FH8SkGGjrZI-1nTeKC4Ov8KzlkeI4M1JVENlMzwxHH1LI9PoTA6KJix9iPdVIMHPcR_kiXuODYJSjYDpEVeWhLU6JsORGjjExCdI6GxzYodKhtm6T59ceN6zkI64O5RyMZ0Lks0B4J8gkCcN1kwEbsWsXFM5BLweGXDu__tE1SGnyGOCwEtLqxw'

#MINIMUM DAILY ISK FLUX TO CONSIDER TRADING IN AN ITEM
minMkt = 1000000

#Target of API requests
esiurl = 'https://esi.evetech.net'

#Naming convention for storage files
scrapelog = 'scrapelog.txt'
scrapeoutput = 'activeTypesScrape.json'
typeidsrc = 'typeIDs.csv'
typeidref = 'typeids.json'
genlog = 'log.txt'
activeitems = 'activeitems.json'
structureOutput = 'structureOrdersOut'
activeItemsVol = 'activeItemsVol.json'
activeItemsComp = 'activeItemsComp.json'
#number of hours after GMT
timeZone = 8

#Length of time after which an non-updated sell order is considered unattended
daysTillAFK = 4

#MARGIN ESTABLISHED IN MONOPOLY CONDITIONS
targetMargin = 0.3

#MARKET COSTS
brokersFee = .02
salesTax = .0335
transportFee = .01