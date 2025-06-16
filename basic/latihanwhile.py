# latihan while

print("========================")
while True:
    user_input = str(input("kamu : "))
    words = user_input.lower().split()

    # LIST SAPAAN
    sapaan_user = ["hai", "halo"]
    sapaan = any(keyword in words for keyword in sapaan_user)

    # OPERASI MATEMATIKA
    operasi_user = ["penjumlahan", "pengurangan"]
    operasi= any(keyword in words for keyword in operasi_user)

    if sapaan :
        print(f"chat : {user_input} juga")
        continue

    if user_input=="dah":
        print(f"{user_input} juga bang")
        break

    if operasi:
        ops = str(words)
        print("========================")
        print("kamu dalam mode operasi")

        while True:
            angka_1 = float(input("masukan angka satu = "))
            angka_2 = float(input("masukan angka dua = "))

            tambah = ['penjumlahan']
            kurang = ['pengurangan']

            plus = any(keyword in ops for keyword in tambah)
            minus = any(keyword in ops for keyword in kurang)

            if plus:
                print(f"hasil dari penjumlahan {angka_1} ditambah {angka_2} adalah ", angka_1 + angka_2 )

            if minus :
                print(f"hasil dari pengurangan {angka_1} ditambah {angka_2} adalah ", angka_1 - angka_2 )

            lnjt = str(input("\nmasih mau lanjut gak (ya/gak : "))

            if lnjt =="ya" :
                continue
            else :
                break

        continue
