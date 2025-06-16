# operasi mengunakan penyinkat
print('==========assigment==========')
a = 5 # assigment
print('niali a =', a)
a += 1
print('niali a += 1 =', a)
a -= 2
print('niali a -= 2 =', a)
a *= 5
print('niali a *= 5 =', a)
a /= 2
print('niali a /= 2 =', a)
b = 10
print('\nnilai b =', b)

#modulus flow division

print('==========modulus &  flow disision==========')
b %= 3
print('nilai b %= 3 , nilai b menjadi', b)
b = 10
print('\nnilai b =', b)
b //= 3
print('nilai b //= 3 , nilai b menjadi', b)
b = 5
print('\nnilai b =', b)
b **= 5
print('nilai b **= 5 , nilai b menjadi', b)

#operasi biwtwise

print('==========bitwise==========')
# or
c = True
print("\nnilai c =", c)
c |= False
print('nilai c |= false nilai C menjadi', c)


# and
c = True
print("\nnilai c =", c)
c &= False
print('nilai c &= false nilai C menjadi', c)

# xor
c = True
print("\nnilai c =", c)
c ^= False
print('nilai c ^= false nilai C menjadi', c)

# geser
d = 0b0100
print("\nnilai d =", format(d, '04b'))
d >>= 2
print('nilai d >>= false nilai e menjadi', format(d, '04b'))

e = 0b0001
print("\nnilai d =", format(e, '04b'))
e <<= 2
print('nilai d <<== false nilai  e', format(e, '04b'))
