import datetime

#multy key
mahasiswa = {
    "nama": "raka kayla",
    "nim": '12345678' ,
    "sks": 132,
    "beasiswa": True,
    "lahir" : datetime.datetime(2006,5,23)
}

# print(mahasiswa)
# print("")

# nasting
mahasiswa1 = {
    "nama": "sri mulyai",
    "nim": '12345278' ,
    "sks": 142,
    "beasiswa": False,
    "lahir" : datetime.datetime(2006,7,13)
}

# dectinoary di dalam deictynary

data_mahasiswa = {
    "mhs1":mahasiswa,
    "mhs2":mahasiswa1
}

print(F"{'KEY':<6} {'NAMA':<17} {'SKS':<3} {'BEASISWA':<9} {'LAHIR':<18} ")
print("-" *50)
for mhs in data_mahasiswa:
    print(F"{mhs:<6} {data_mahasiswa[mhs]["nama"]:<17} {data_mahasiswa[mhs]["sks"]:<3} {data_mahasiswa[mhs]["beasiswa"]:^9} {data_mahasiswa[mhs]["lahir"]}")
    

