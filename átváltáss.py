érték = input("Adjon meg egy számot:")
érték = int(érték)
mértékegység = input("Adja meg a mértékegységet(cm/inch):")


if mértékegység =="cm":
        eredmény = érték/2.54
        print(f"{eredmény} inch")
elif mértékegység =="inch":
        eredmény = érték*2.54
        print(f"{eredmény} cm")
else:
    print("Hiba")



