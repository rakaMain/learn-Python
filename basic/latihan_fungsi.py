'''latihan fungsi'''

import os#

# luas menghitung luas dan keliling persegi panjang
# os.system("cls")
# print(f"==== PROGRAM MENGHITUNG LUAS PERSEGI PANJANG ====")

# def lk_persegi_panjang(l,k):
#     luas = k*l
#     keliling= (k*2)+(l*2)
    
#     hasil = f"luasnya {luas}, kelilingnya {keliling}"
#     return hasil
    
# panjang_user = int(input("masukan panjang persegi nya = "))
# lebar_user = int(input("masukan lebar persegi nya = "))

# hasil_user = lk_persegi_panjang(lebar_user,panjang_user)
# print(hasil_user)

# menggunakan fungsi semuanya

def header():
    os.system("cls")
    print(f"==== PROGRAM MENGHITUNG LUAS PERSEGI PANJANG ====")

def user_input():
    panjang_user = int(input("masukan panjang persegi nya = "))
    lebar_user = int(input("masukan lebar persegi nya = "))
    hasil = [panjang_user, lebar_user]
    return hasil


def hitung_luas(p,l):
    hasil = p*l
    return hasil

def hitung_keliling(p,l):
    hasil = (p*2)+(l*2)
    return hasil

def display(n):
    print(f"maka hasil nya = {n}")

    
while True :
    header()
    user = user_input()
    opsi = str(input("mau hitung apa [luas][keliling][keduanya] = "))
    if opsi == "luas":
        hasil = hitung_luas(user[0], user[1])
        display(hasil)

    if opsi == "keliling":
        hasil = hitung_keliling(user[0], user[1])
        display(hasil)

    if opsi == "keduanya":
        hasil = f"maka luas nya = {hitung_luas(user[0], user[1])}, maka keliling nya = {hitung_keliling(user[0], user[1])} "
        print(hasil)
    

    isContinue = str(input(f"mau lanjut gak (gak/ya) = "))
    if isContinue == "gak":
        print(f"papay sayangku")
        break
    










