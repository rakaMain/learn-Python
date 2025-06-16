# data and time

import datetime as dt

hari_ini = dt.date.today()
print(hari_ini)

print(f"hari ini adalah hari = {hari_ini:%A}")

tanggal = dt.date(2006,5,23)
print(tanggal)
print(f"hari ini adalah hari = {tanggal:%A}")

print('===========tebak hari lahir mu==============')
tanggal_user = int(input('masukan tanggal :'))
bulan_user = int(input('masukan bulan :'))
tahun_user = int(input('masukan tahun :'))

hari_user = dt.date(tahun_user, bulan_user, tanggal_user)
print(hari_user)

print(f'hari lahir mu adalah hari = {hari_user:%A}')

umur_user = int((hari_ini - hari_user).days / 365)
print(f'kamu berumur =', umur_user, 'tahun')
