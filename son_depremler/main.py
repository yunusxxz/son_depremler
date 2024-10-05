import re

import requests as req
from bs4 import BeautifulSoup as bs

url = 'http://www.koeri.boun.edu.tr/scripts/Sondepremler.asp'

response = req.get(url)

if response.status_code == 200:
    content = response.content
    soup = bs(content, "html.parser")
    pre = soup.find('pre')
    #print(pre)
    #print(pre.text)
    text = pre.text
    lines = text.splitlines()[7:-1] # 508 satırlık verinin ilk ve son boş satır, sonra ki 6 başlık satırı boş.
    #print(len(lines), lines)

    earthquakes = []
    for line in lines:
        cols = re.split("\\s{2,}", line) #Yani, iki veya daha fazla boşluk karakterinin bulunduğu yerlerde dizeyi böler ve her bir bölümün bulunduğu bir liste döndürür.
        #print(cols)
        eq = {
            "tarih_saat": cols[0],
            "enlem": float(cols[1]),
            "boylam": float(cols[2]),
            "derinlik": float(cols[3]),
            "şiddet": float(cols[5]),
            "yer": cols[7]
        }
        earthquakes.append(eq)

    print(earthquakes)