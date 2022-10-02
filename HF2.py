def haromszog(a,b,c):
    if a+b>c and a+c>b and c+b>a:
        return True
    else:
        return False

a_oldal = float(input("Adja meg az a oldal hosszát:"))
b_oldal = float(input("Adja meg a b oldal hosszát:"))
c_oldal = float(input("Adja meg a c oldal hosszát:"))

if __name__ == "__main__":
    if haromszog(a_oldal,b_oldal,c_oldal):
        print("A háromszög megszerkeszthető")
    else:
        print("A háromszög nem szerkeszthető meg")


