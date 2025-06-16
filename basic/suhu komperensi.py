# latihan konvrensi temperatur

#c
# celcius = float(input("masukakn  suhu dalam celcius : "))
# print("suhu dalam celcius adalah = ", celcius)

# # dalam reamur
# reamur = celcius * 4 / 5 
# print("suhu dalam reamur adalah = ", reamur)

# # dalam farenhait
# farenhait  = ( 9 / 5 * celcius ) + 32
# print("suhu dalam farenhait adalah = ", farenhait)

# # dalam kelvin
# kelvin  = celcius + 273
# print("suhu dalam kelvin adalah = ", kelvin )


# rumus farenhait ke kelvin
farenhait = float(input("masukan nilai farenhait = "))

print("nilai faremhait adalah = ", farenhait)

kelvin = ( 5 / 9 * ( farenhait - 32)) + 273 
print("nilai kelvin adalah = ", kelvin)

kelvin_1 = float(input("masukan nilai kelvin = "))

print("nilai kelvin adalah = ", kelvin_1)

farenhait_1 = ( 9 / 5 * ( kelvin_1 - 273.15 ) ) + 32
print("nilai faremhait adalah = ", farenhait_1)

