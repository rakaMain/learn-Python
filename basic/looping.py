# looping

angka = [0,8,2,9,4]
print(angka)
for i in angka :
    b = i
    b %= 2
    if b==0 :
        print(f"{i} bernilai genap")
    else :
        print(f"{i} bernilai ganjil")
print('akhir program list')

print("===================")
for i in range(1,11) :
    b = i
    b %= 2
    if b==0 :
        print(f"{i} bernilai genap")
    else :
        print(f"{i} bernilai ganjil")
print('akhir program')

# menggunakan string
print("===================")
data_str = "sayaa gantenggggg"

for huruf in data_str :
    print(huruf)