# # latihan looping bentuk

sisi = 10
cont = 10

print("=====looping for======")
for i in range(sisi):
    print("*" * cont)
    cont -= 1
print("=====looping akhir=====")

c = 11
while True :
    c -= 1
    if c!=0 :
        if 0==(c % 2) :
            print("*" * c)
            continue
        else :
            continue
    else :
        break

print("=====while ganjil====")
c = 11
while True :
    c -= 1
    if c!=0 :
        if 0!=(c % 2) :
            print("*" * c)
            continue
        else :
            continue
    else :
        break

print("=====segitiga======")

angka = 0
acuan = -2
spasi = 6
while True:
    angka += 1
    acuan += 2
    if angka <= 10 :
        print("*"*angka)
        continue
    if angka <= 20:
        ulang = angka - (acuan - 20)
        print("*"* ulang)
        continue

    else :
        break


angka = 0
acuan = -2
spasi = 6
while True:
    angka += 1
    acuan += 2
    spasi -= 1
    if angka <= 10 :
        if 0!=(angka % 2) :
            bas_kiri= "-"* spasi
            bas_kanan = "-"* spasi
            pr = "*"*angka
            print(bas_kiri, pr, bas_kanan, spasi,spasi)
        else :
            spasi += 1
        continue
    if angka <= 21 :
        if 0!=(angka % 2) :
            ulang_spasi = spasi * (-1)
            ulang = angka - (acuan - 20)
            bas_kiri= "-"* ulang_spasi
            bas_kanan = "-"* ulang_spasi

            pr = "*"*ulang 
            print(bas_kiri, pr, bas_kanan,ulang_spasi, spasi)
        else :
            spasi += 1
        continue
    else :
        break