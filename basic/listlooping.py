ka = [3,4,3,2,1,3,4,5,6]

for angka in ka:
    print(angka)


# for loop dan range

panjang = len(ka)

for i in range(panjang):
    print(f"angka = {ka[i]}")

# ehile loop

i = 0
while i < panjang:
    print(f"angka = {ka[i]}")
    i += 1

# list comperhensi

data = ["raka",3,4,5,4]
[print(i) for i in data]

# enumarate
data = ["raka",3,4,5,4]

for index,data in enumerate(data):
    print(f"index = {index}, data = {data}")

















