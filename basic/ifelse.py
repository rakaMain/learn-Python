# nama = input('siapa nama kamu = ' )

# # if nama =="raka" : print('hai rakaa')
# # else : print('salah orang')

# if nama== "raka" :
#     print('berhasil')
# print("terimaskih ", nama)

# angka = int(input('masukan angka = '))
# angka %= 2

# if angka==0 :
#     print('genap')
# else :
#     print('ganjil')

print("===========KALKULASI===========")

masukan_tahun = int(input('masukan tahun lahir mu = '))
masukan_hari= str(input("masukan hari lahir kamu = "))
masukan_angka = int(input("masukan tanggal lahir kamu = "))



print("\n===========tanggal=============")

if masukan_angka<=32 :
    masukan_angka %= 2

if masukan_angka==0 :
    print('tanggal lahir kamu = genap')

elif masukan_angka==int :
    print('anggal lahir kamu = ganjil')

else :
    print("tanggal tidak ada yang lebih dari 32")

print("===========hari=============")
if masukan_hari== 'minggu' or masukan_hari== "sabtu" :
    print("kamu lahir di waktu weekend")

elif  masukan_hari=="" :
    print("kamu lahir di waktu weekend")

else :
    print("harus berisi nama nama hari")

print("===========tahun=============")
masukan_tahun %= 4
if masukan_tahun==0 :
    print("kamu lahir ditahun = kabisat")
else :
    print('kamu lahir dibukan tahun = kabisat')
