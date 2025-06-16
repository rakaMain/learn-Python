'''mengimput banyak arg''' 

def fungsi(nama, tinggi, berat ):
    print(f"{nama} adalah nama, {tinggi} adalah tinggi, {berat} adalah berat")
fungsi("raka", 170, 50)


''' di buat jadi list ribet banget '''
# def fungsi1(data_list):
#     data = data_list.copy()
#     nama = data[0]
#     n

def item(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(F"{nama}, memiliki tinggi {tinggi}, memiliki berat {berat}")

item("raka", 172, 50)

def tambah(*args): # mengabim banyak input
    hasil = 0
    for angka in args:
        hasil += angka
    return hasil

print(tambah(13,34,24,25,21,3,13,23,23,23,24,3,4,5,4,4,54,5))

