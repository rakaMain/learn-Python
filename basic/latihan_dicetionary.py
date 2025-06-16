# template dict mahasisiwa
import datetime

mahasiswa_template = {
    'nama':'nama',
    'nim': '00000000',
    'sks_lulus':0,
    'lahir':datetime.datetime(1111,11,1)
}
print(mahasiswa_template)

data_mahasiswa = {}

print(f"=====SELAMAT DATANG DI PENGISIAN DATABASE CEPAT=====\n")
while True:
    import datetime
    print("bot = mau ngapain? [buat data][liat data][hapus data]")
    user_input = str(input("you = "))
    if user_input == "buat data":
        mhs_data = mahasiswa_template.copy()
        # data yang ditanyakan
        print("MASUKAN DATA DIRI")
        type_0 = str(input("masukan no anda = "))

        nama_0 = str(input("nama = "))
        nim_0 = str(input("nim = "))
        sks_0 = int(input("sks = "))

        print("MASUKAN KELAHIRAN")
        lahir_tahun = int(input("tahun = "))
        lahir_bulan = int(input("bulan = "))
        lahir_tangga = int(input("tanggal = "))


        lahir_1 = datetime.datetime(lahir_tahun,lahir_bulan,lahir_tangga)


        mhs_data["nama"] = nama_0
        mhs_data["nim"] = nim_0
        mhs_data["sks_lulus"] = sks_0
        mhs_data["lahir"] = lahir_1

        print(mhs_data)
        data_mahasiswa.update({type_0 : mhs_data})
        print(data_mahasiswa)

        continue