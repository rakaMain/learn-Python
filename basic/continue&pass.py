# kontrol flow

# continue, pass, break

# pass tidak akan di eksekusi 

angka = 0 

while angka < 5:
    angka += 1
    if angka==3 :
        pass # tidak akna di eksekusi
    print(angka)

print("===========continue==========")

angka = 0

print(f"angka sekarang = {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarnag = {angka}")
    print("wawa")

print("udah")

angka = 0

print(f"angka sekarang = {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarnag = {angka}")
    if angka==2:
        print("ini 2")
        continue
    print(f"bukan angka prioritas = {angka}")
print("udah")

while True:
    chat = (input("kamu = "))
    if chat=="dah" :
        print("dadah bang")
        break
    if chat=="hai" :
        print("saya = hai juga")
        continue
    print("coba ketik hai")
    