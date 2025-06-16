''' global scope '''

nama = "raka"

''' var global '''

def fungsi(n):
    return n

print(fungsi(nama))

for i in range(0,5):
    print(f"looping {i} - {nama}")

''' varable local '''

def fungsi2():
    nama_l = "sri"

fungsi2()