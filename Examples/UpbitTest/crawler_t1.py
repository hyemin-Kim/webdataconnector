import requests
import os

# check_file = os.path.isfile("D:\\4. My github\\webdataconnector\\Examples\\upbit test\\upbit_data_t1.json")

# check_file = "upbit_data_t1.json"



#if check_file is True:
#   file = open("upbit_data_t1.json", 'w')
#if check_file is False:
#    file = open("upbit_data_t1.json", 'w+')

file = open("upbit_data_t1.json", 'w')

def func1():
    market = {"KRW-ADA", "KRW-BTC", "KRW-AXS", "KRW-DOGE", "KRW-ETC", "KRW-ETH", "KRW-LINK", "KRW-LTC", "KRW-MANA", "KRW-NEO", "KRW-TRX", "KRW-VET", "KRW-XRP"}
    url = "https://api.upbit.com/v1/candles/days"
    for i in market:
        querystring = {"market":i,"count":"20"}
        headers = {"Accept": "application/json"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        file.write(response.text)
    #file.close()

func1()

files = open("upbit_data_t1.json", 'r')
lines = files.readlines()
string = "Too many"

for lines in lines:
    if string in lines:
        func1()
    else:
        print("Success")
        break

start = open("upbit_data_t1.json", "r", encoding="UTF-8")

for line in start:
    line = line.strip()
    changes = line.replace("][", ",")
start.close()

end = open("upbit_data_t1.json", "w", encoding="UTF-8")
end.write(changes)
end.close()