# s24014
# 沖縄県の推計人口のページにより最新情報をスクレイピングする
#　https://www.pref.okinawa.jp/toukeika/estimates/estimates_suikei.html
import requests

url = "https://www.pref.okinawa.jp/toukeika/estimates/estimates_suikei.html"
response = requests.get(url)

response.encoding = response.apparent_encoding
# 出力部分
print(response.text)
