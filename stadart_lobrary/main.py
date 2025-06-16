import datetime

data_waktu = datetime.datetime.now()
print(data_waktu)
print(data_waktu.year)
print(data_waktu.strftime('%A'))

from collections import Counter

data = ["a","b","c","d","a","b"]

data_count = Counter(data)

print(data_count)
print(data_count['a'])

import io


file = io.open("stadart_lobrary\main.txt","r")

print(file.read())