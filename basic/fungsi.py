# fungsi python

# def hello_world():
#     print("hellow world")
#     print("hai aku raka km")


# hello_world()
# hello_world()

# definisi di gunakan setelah mendefinisikan

# fungsi dan argument nya

''' fungsi dengan argument '''

def fungsi_nama(arg):
    # body fungsi
    print(f"halo {arg}")

fungsi_nama("raka")

def perhitungan_angka(angka1,angka2):
    '''fungsi tambah'''
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")

perhitungan_angka(3,5)


def sayHay(arg):
    arg_sample = arg.copy()
    for i in arg_sample:
        print(f"hai {i}")

list_nama = ["raka","ceri"]

sayHay(list_nama)

