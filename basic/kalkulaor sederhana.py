# latiahn kalkulator sederhana
print("===========KALKULATOR SEDERHANA===========")

a = 0

angka_satu = int(input("masukan angka = "))
angka_dua = int(input("masukan angka = "))
operasi = str(input("isi ( kali, bagi, tambah, kurang) = "))

if (operasi== str(operasi)) & (angka_satu==int(angka_satu)) & (angka_dua==int(angka_dua)) :
    print("akan segera di kerjakan")
    a =+ 1
else :
    print("ulangi lagi ada kesalahan mengimput")

if a==1 :
    if operasi=="kali" :
        hasil = angka_satu * angka_dua
        print('hasil nya adalah ', hasil)
    elif operasi=="bagi" :
        hasil = angka_satu % angka_dua
        print('hasil nya adalah ', hasil)
    elif operasi=="tambah" :
        hasil = angka_satu + angka_dua
        print('hasil nya adalah ', hasil)
    elif operasi=="kurangi" :
        hasil = angka_satu - angka_dua
        print('hasil nya adalah ', hasil)
    else :
        print("isi dengan benar")

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


