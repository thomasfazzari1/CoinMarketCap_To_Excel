from requests import Request, Session
from openpyxl import Workbook
import pprint
import json

#creation du fichier excel
wb = Workbook()
#feuille 1
ws = wb.active
ws.append(["DEVISE","PRIX","MARKETCAP","VOLUME SOUS 24H"])

key = input("Saisissez votre clé d'API (https://pro.coinmarketcap.com/account) : ")
quotesLatestUrl = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'

#tableau des cryptomonnaies ciblées, à modifier en dur dans le script
devises = ("BTC","ETH","BNB","USDT","XRP","ADA","ORAI","MATIC","DOT","AVAX","TRX","UNI","ATOM","LINK")

for crypto in devises:
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
	price = round((json.loads(response.text)['data'][crypto][0]['quote']['USD']['price']),2)
	marketcap = json.loads(response.text)['data'][crypto][0]['quote']['USD']['market_cap']
	volume24h = json.loads(response.text)['data'][crypto][0]['quote']['USD']['volume_24h']
	# ajout d'une ligne contenant la devise et le prix correspondant
	ws.append(["$"+ crypto, price, marketcap,volume24h])
	wb.save('data.xlsx')