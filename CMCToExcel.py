from requests import Request, Session
from openpyxl import Workbook
import pprint
import json

#creation du fichier excel
wb = Workbook()
#feuille 1
ws = wb.active

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
price = json.loads(response.text)['data'][crypto][0]['quote']['USD']['price']
pprint.pprint("Prix actuel de "+crypto+" : " + str(round(price,2)) + " $.")

# ajout d'une ligne contenant la devise et le prix correspondant
ws.append(["DEVISE","PRIX"])
ws.append(["$"+crypto, price])
wb.save('prices.xlsx')