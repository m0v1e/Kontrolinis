import pickle

while True:
    veiksmas = int(input("Pasirinkite veiksma: 1 - perziureti, 2 - irasyti, 3 - iseiti"))
    try:
        if veiksmas == 1:
            with open("zmones.pkl", "rb") as failas:
                print(pickle.load(failas))
        if veiksmas == 2:
            with open("zmones.pkl", "rb") as failas:
                zmones = pickle.load(failas)
                naujas_vardas = input("Iveskite nauja varda: ")
                zmones.append(naujas_vardas)
                with open("zmones.pkl", "wb") as failas2:
                    pickle.dump(zmones, failas2)
    except FileNotFoundError:
        print("nera tokio failo")
        with open("zmones.pkl", "wb") as failas:
            print("tiesiog susikuria failas")
    except EOFError:
        print('nera reiksmiu')
        with open("zmones.pkl", "wb") as failas:
            print("idedam tuscia sarasa")
            zmones = []
            pickle.dump(zmones, failas)
    if veiksmas == 3:
        print("Programa baigta")
        break