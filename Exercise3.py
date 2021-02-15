from datetime import datetime
import urllib.request
import json
from time import sleep
year = str(datetime.now().year)
month = datetime.now().month
day = datetime.now().day
if month < 10:
    month = "0" + str(month)
else:
    month = str(month)
for i in range(1, day+1):
    if i < 10:
        day2 = "0" + str(i)
    else:
        day2 = str(i)
    url = "https://api.opap.gr/draws/v3.0/1100/draw-date/"+year+"-"+month+"-"+day2+"/"+year+"-"+month+"-"+day2+"/draw-id"
    r = urllib.request.urlopen(url)
    html = r.read()
    html = html.decode
    d = json.loads(html)
    x = str(d[0])
    url = "https://api.opap.gr/draws/v3.0/1100/"+x
    r = urllib.request.urlopen(url)
    html = r.read()
    html = html.decode
    d = json.loads(html)
    print(year+"-"+month+"-"+day2+": ", d["winningNumbers"]["list"])
    sleep(5)
