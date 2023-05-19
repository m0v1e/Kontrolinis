import pickle




print('Noredami iseiti is ivedimo proceso ties vardu iveskite exit')
sarasas = {

}

while True:
    naujas_vardas = input('Iveskite darbuotojo varda: ')
    raktas = "vardas1"
    sarasas.update({raktas : naujas_vardas})
    if naujas_vardas == "exit":
        break
        # amzius = int(input('Iveskite darbuotojo amziu: '))
        # pickle.dump(amzius, failas)
        # darbo_pozicija = input('Iveskite darbuotojo pozicija: ')
        # pickle.dump(darbo_pozicija, failas)

print(sarasas)

