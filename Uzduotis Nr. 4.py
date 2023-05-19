import statistics

sarasas = [([1, 2, 3]), ([4, 5, 6]), ([7, 8, 9])]

naujas_sarasas = [x for tpl in sarasas for x in tpl]

print(naujas_sarasas)

what = []

for x in naujas_sarasas:
    print(type(x))
    if x == str:
        what.append(x)
    elif x == list:
        vidurkis = statistics.mean(x)
        print(vidurkis)
        vidurkis.append(what)


print(what)