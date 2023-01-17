from requests import Request, Session
import pprint
import json

key = input("Saisissez votre clé d'API (https://pro.coinmarketcap.com/account) et appuyez sur entrée : ")
quotesLatestUrl = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'

data = {
	'symbol':'BTC',
	'convert':'USD'
}

headers = {
	'Accepts':'application/json',
	'X-CMC_PRO_API_KEY':key
}

session = Session()
session.headers.update(headers)
response = session.get(quotesLatestUrl, params = data)
pprint.pprint(json.loads(response.text))