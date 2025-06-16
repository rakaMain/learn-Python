data = ["raka", "bayi", "ceri"]
# index nya dari 0

data_0 = data[0]
print("data pertama adalah = ", data_0)

#langsung di definisikan
print("data terakhir adalah = ", data[-1])

# mengambil info jumlah
panjang_data = len(data)
print(panjang_data)

#manipulasi data list

#menamabahkan item sesuai posisi
print(f"data sebelum ditambah = \n{data}")

data.insert(1, "asep")
print(f"data sudah ditambahakn = \n{data}")

#menamabah di akhir
data.append("mulyani")
print(f"data ditamabahkan lagi = \n{data}")


#menamabhakan lis denga ist
data_baru = ["dadan", "ucup"]
data.extend(data_baru)
print(f"data setelah di gabungkan = \n{data}")

# merubah data 
data[2] = "michel"
print(f"data rubah = \n{data}")

#menghilangkan data 
data.remove("raka")
print(f"data rubah = \n{data}")

data.pop() # mengabil data di akhri atau di pidahakan
print(f"data rubah = \n{data}")
