import requests

headers = {
'accept': 'application/json',
}
params = (
    ('datasource', 'tranquility'),
    ('page', '1'),
)

queryString = 'https://esi.evetech.net/latest/markets/10000039/types/?datasource=tranquility&page=1'
print(queryString)



response = requests.get(queryString, headers=headers, params=params)



#if(type(some_data) == str):
		#	file.write(some_data)