# program list buku
data_buku = []
while True:
    print("mau ngapain disini bang ? ")
    print("[mau beli] [mau jual] [mau keluar] [liat]")

    # mau jualan
    user_respon = str(input("you = "))
    if user_respon == "mau jual":
        judul_buku = str(input("masukan judul buku\t= "))
        penulis_buku = str(input("masukan nama penulis nya \t= "))

        buku_baru = [judul_buku, penulis_buku]
        data_buku.append(buku_baru)
        print(data_buku)
        print(f"buku baru telah di tambahkan = {buku_baru} ")
        print("==========================")

        continue

    if user_respon == "mau beli":
        for index,buku in enumerate(data_buku):
            print(f"{index} | {buku[0]} | by {buku[1]}")
        user_pilih = int(input("mau beli buku no berapa = "))
        for index,buku in enumerate(data_buku):
            if user_pilih == index:
                print(f"{data_buku[index]} telah dibeli")
                data_buku.remove(data_buku[index])
            else:
                print("gagal")
        continue

    if user_respon == "liat":
        for index,buku in enumerate(data_buku):
            print(f"{index} | {buku[0]} | by {buku[1]}")

    if user_respon == "keluar":
        break

        


