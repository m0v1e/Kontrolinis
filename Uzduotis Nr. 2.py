
sarasas = (4, 3, 2, 1, 4, 6, 2)

def duplikatai(a):
    naujas_sarasas = []
    for reiksme in a:
        naujas_sarasas.append(reiksme)
    naujas_sarasas = [*set(naujas_sarasas)]
    return tuple(naujas_sarasas)

print(duplikatai(('a', 'b', 'c', 'e', 'r', 'm', 'a', 'a', 'f')))