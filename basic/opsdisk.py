#operator dictioaery
data_disc = {
    "rk" : "raka",
    "cr" : "ceri",
    "by" : "bayu"
}

lendict = len(data_disc)
print(f"panjang disc = {lendict}")

# mengecek key ada atau engga

KEY = "rk"
CHECKEY =  KEY in data_disc
print(f"apakah {KEY} ada di data_disc: {CHECKEY}")

# mengaskese value

print(data_disc["rk"])
print(data_disc.get("rk")) # lebih gampang
print(data_disc.get("bb", "key = gak ada bang"))

# mengupdate data

data_disc["rk"] = "rakaa km"
print(data_disc)

#nambah
data_disc["bb"] = "bayuyuyu"
print(data_disc)
data_disc.update({"rk" : "raka kayla mahmmud"})
print(data_disc)

#menghapus

del data_disc["by"]
print(data_disc)

















