class munka:
    def __init__(self,nev, munkahely, pozicio):
        self._nev = nev
        self._munkahely = munkahely
        self._pozicio = pozicio

    def __str__(self):
        return self._nev + "a" +str(self._munkahely) + "-en dolgozik " + str(self._pozicio)

    def details(self):
        print("--Developer létrehozva--")
        print(self._nev, "a", self._munkahely,"-en dolgozik", self._pozicio,"szerepkörben")

    def __eq__(self, other):
        if self._munkahely == other._munkahely:
            print(self._nev,"és",other._nev,"egy projekten dolgoznak")
        else:
            print(self._nev,"és",other._nev,"nem egy projekten dolgoznak")



alkalmazott1 = munka("Ricsi","SolArch","Frontend szerepkörben")
alkalmazott2 = munka("Angéla","Zerteng","Tesztelő")
alkalmazott3 = munka("Peti","KefeRP","Frontend")
alkalmazott4 = munka("Éva","KefeRP","Frontend")

alkalmazott1.details()
alkalmazott2.details()
alkalmazott3.details()
alkalmazott4.details()

alkalmazott3 == alkalmazott4