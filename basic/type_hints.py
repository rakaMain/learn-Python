def fungsi(p):
    hasil = p**2
    print(hasil)

fungsi(1)
# fungsi("bayu")

''' type hint kita bisa memberika format argument'''

def hints(arg:int) -> int :
    output = 10**arg
    return output

hasil = hints(2)
print(hasil)

''' type argument aja '''

def display(arg:str):
    print(arg)

print(display("raka"))

# import os

# hasil = os.system("cls")
# print(hasil)
