from requests import Request, Session
import pprint
import json

key = input("Saisissez votre clé d'API (https://pro.coinmarketcap.com/account) : ")
quotesLatestUrl = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'

crypto = input("Saisissez la devise (ex: BTC): ")

data = {
	'symbol':crypto,
	'convert':'USD'
}

headers = {
	'Accepts':'application/json',
	'X-CMC_PRO_API_KEY':key
}

session = Session()
session.headers.update(headers)
response = session.get(quotesLatestUrl, params = data)
pprint.pprint('Prix actuel de '+crypto)
pprint.pprint(json.loads(response.text)['data'][crypto][0]['quote']['USD']['price'])