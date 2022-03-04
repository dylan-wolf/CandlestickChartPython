import requests, json, csv



TOKEN = "YOUR IEX CLOUD API CODE"

SYMBOL = 'RTX'


URL = "https://sandbox.iexapis.com/stable/stock/{}/chart/5y?token={}".format(SYMBOL, TOKEN)

r = requests.get(URL)

# Changes string to python data structure
json_data = json.loads(r.content)
# Writes python dictionary to csv file
csv_file=open(SYMBOL + '.csv' ,'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(('date', 'open', 'high','low','close'))
for item in json_data:
    print(item)
    csv_writer.writerow((item['date'], item['open'], item['high'], item['low'], item['close']))

csv_file.close()
