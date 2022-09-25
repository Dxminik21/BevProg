mondat =input("Irjon be egy mondatot:")

betuk = {}
for i in mondat:
    betuk[i] = mondat.count(i)
print("Betuk gyakorisága:",betuk)

forditva = print("Forditva:",{mondat[::-1]})

print(mondat.split())