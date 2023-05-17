
def raides(sarasas):
    raidziu_sarasas = []
    for vardas in sarasas:
        vardas.split()
        raidziu_sarasas += vardas[0]
    return(raidziu_sarasas)



print(raides(["Tomas", "Mindaugas", "Gerda", "Karolina", "Vidas", "Robertas", "Asta", "Zydrunas"]))