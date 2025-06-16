data_angka = [1,3,4,5,7,9,5,6,7,4,7,9,4,2,5,6,7]

print(data_angka)

#count data
angka = int(input("angka apa yang kamu pilih = "))

jumlah_data_5 = data_angka.count(angka)
print(f"jumlah data angka {angka} = {jumlah_data_5}")
print(f"posisi {angka} ada di     = {data_angka.index(angka)}")


# ambil posisi data
print("==================")
data = ["raka", "bayi", "ceri"]
print(data)
index_raka = data.index("raka")
print("posisi raka ada di = ", index_raka)

# mengurutkan list

print(f"data angka sebelum di sort = {data_angka}")
data_angka.sort()
print(f"data angka sesudah di sort = {data_angka}")

# urtuan yang stringe 

print(f"data angka sebelum di sort = {dxata}")
data.sort()
print(f"data angka sesudah di sort = {data}")


# di balik urutan nya 

print("============================")
data_angka.reverse()
print(f"data angka sesudah di sort = {data_angka}")

data.reverse()
print(f"data angka sesudah di sort = {data}")






















