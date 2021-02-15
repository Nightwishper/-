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
    url = "https://api.opap.gr/draws/v3.0/1100/draw-date/"+year+"-"+month+"-"+day2+"/"+year+"-"+month+"-"+day2
    r = urllib.request.urlopen(url)
    html = r.read()
    html = html.decode()
    d = json.loads(html)
    numbers = []
    max = 0
    for i2 in range(len(d["content"])):
        for i3 in d["content"][i2]["winningNumbers"]["list"]:
            numbers.append(i3)
    for i2 in numbers:
        x = numbers.count(i2)
        if x > max:
            max = numbers.count(i2)
            maxnumber = i2
    print(year+"-"+month+"-"+day2+": ", maxnumber)
    sleep(3)
