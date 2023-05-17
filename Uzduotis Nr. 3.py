import pickle




print('Noredami iseiti is ivedimo proceso ties vardu iveskite exit')

while True:
    with open('sarasas.pkl', 'ab') as failas:
        naujas_vardas = input('Iveskite darbuotojo varda: ')
        pickle.dump(naujas_vardas, failas)
        if naujas_vardas == "exit":
            break
        # amzius = int(input('Iveskite darbuotojo amziu: '))
        # pickle.dump(amzius, failas)
        # darbo_pozicija = input('Iveskite darbuotojo pozicija: ')
        # pickle.dump(darbo_pozicija, failas)

with open("sarasas.pkl", "rb") as failas:
    print(pickle.load(failas))

