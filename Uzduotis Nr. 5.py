import pickle
import functools

vidurkis = '50'

with open("skaiciai.txt", "r") as failas:
    failas.read()
    # functools.reduce(lambda: a, b: a + b, failas)
    skaiciu_sarasas = [x for x in failas if x == int]
    print(skaiciu_sarasas)

with open("vidurkis.txt", 'w') as failas:
    failas.write(vidurkis)

