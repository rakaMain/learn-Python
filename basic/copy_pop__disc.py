# copy dixtionary
teman_teman = {
    "raka" : "raka kayla mahmud",
    "sri"  : "sri mulyani",
    "ceri" : "ceri mulyani"
 }

#friends = teman_teman
friends = teman_teman.copy() #copy itu memakai atau mengambil

print("teman teman = ", teman_teman)
print("friends", friends)
print(" ")

teman_teman["raka"] = "raka mamud"

print("teman teman = ", teman_teman)
print("friends", friends)
print(" ")

# pop dictionary
data_raka = friends.pop("raka")
print(f"data raka = {data_raka}") # mentrsabper data
print("friends = ", friends)
print(" ")

data_terakhir = friends.popitem()
print(f"data terkahir = {data_terakhir}") # mentrsabper data
print("friends = ", friends)



























