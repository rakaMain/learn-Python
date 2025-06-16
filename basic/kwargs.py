'''**wargs'''

def fungsi1(nama, tinggi, berat):
    '''fungsi bisasa'''
    print(f"{nama}, tigginya {tinggi} berat nya {berat}")

fungsi1("raka", 173, 50)

def fungsi2(**kwargs):
    ''' fungsi kwargs'''
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]

    print(f"{nama}, tigginya {tinggi} berat nya {berat}")

fungsi2(nama="raka", tinggi=173, berat=50)

def math(*args,**kwargs):
    angka = args
    hasil = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            hasil += angka
    
    elif kwargs["option"] == "kali":
        for angka in args:
            hasil += 1
            hasil *= angka
        
    elif kwargs["option"] == "kurangi":
        for angka in args:
            hasil -= angka

    return hasil
            

print(math(2,3,4,option="tambah"))
print(math(2,3,4,option="kali"))
print(math(2,3,4,option="kurangi"))
