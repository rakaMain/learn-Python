def f_kuadrat(angka):
    return angka**2
print(f_kuadrat(2))

# lamda fungsi

kuadrat = lambda angka:angka**2
print("hasil lamda =", kuadrat(3))

pangkat = lambda num,po : num**po
print(pangkat(2,4))

# kegunaan nya apa
# sorting untuk list

data_list = ["raka", "kayla", "bayi"]
data_list.sort()
print("hasil sort", data_list)

# sorting pakai panjang

def pn(nama):
    return len(nama)

data_list.sort(key=pn)
print("hasil sort by len", data_list)

# sorting pakau lamda
data_list = ["raka", "kayla", "bayi"]
data_list.sort(key=lambda nama: len(nama))
print(f"sorting menggunakan lamda = {data_list}")

data_angka = [1,2,3,4,5,6,7,8,9,10]
# kasusu kurang

data_angka_baru = list(filter(lambda angka: angka< 5, data_angka))
print(data_angka_baru)

# kasusu genap

data_angka_genap = list(filter(lambda angka: (angka%2==0), data_angka))
print(data_angka_genap)

# kasusu ganjil
data_angka_ganjil = list(filter(lambda angka: (angka%2!=0), data_angka))
print(data_angka_ganjil)

# anonymous funciton
# currying 


def pangkat(n):
    return lambda angka: angka**n

pangkat2 = pangkat(3)
print(pangkat2(3))
print(pangkat(2)(5))

# fungsi di dalam fungsi













