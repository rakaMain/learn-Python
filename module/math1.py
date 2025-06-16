
def plus(*args):
    hasil = 0
    for i in args:
        hasil += i
    return hasil

def times(*args):
    hasil = 1
    for i in args:
        hasil *= i

    return hasil

def pangkat(n:int):
    return lambda angka:angka**n
