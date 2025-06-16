# funsgi dan return

def fungsi(arg):
    return

#fungsi kuadrat

def fungsi_kuadrat(arg):
    outut = arg**2
    return outut

y = fungsi_kuadrat(5)
print(y)


# default argument
print("------------------------------------------")
''' arg kepada input, kalo gak isi gimana?'''
def fungsi(nama = "kamu"):
    print(f"halo {nama}")

fungsi("raka")

fungsi()#gimana caranya
print("------------------------------------------")

def sapDia(pesan, nama = "kamu"):
    '''satu biasa satu default argument'''
    print(f"Hai {nama}, {pesan}")

sapDia("halo bang bang", "raka")
sapDia("YaAllah semoga keterima utbk")

print("------------------------------------------")

def pangkat(angka, pangkat):
    hasil = angka**pangkat
    return hasil

print(pangkat(3,3))

print("------------------------------------------")

'''menggunakan parameter'''
print(pangkat(pangkat= 3, angka=2))

print("------------------------------------------")

def fungsi_1(n1=1,n2=2,n3=3,n4=4):
    hasil = n1+n2+n3+n4
    return hasil

print(fungsi_1())
print(fungsi_1(n1=5))













































