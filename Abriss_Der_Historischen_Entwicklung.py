from random import choice

def frage(d):
    a = choice(list(d.keys()))
    print("Wer lebte im Jahre:", a, "?")
    aw = input("lebte: ")
    if aw not in d[a]:
        print("Falsch!")
        print("Im Jahr", a, "lebte(n):", ', '.join(d[a]))
    else:
        print("Richtig!")
        del d[a]

# Dictionary
dicA = {
    '460-370 v. Chr.': ['Demokrit'],
    '490-430 v. Chr.': ['Empedokles'],
    'Um 480 v. Chr.': ['Parmenides', 'Heraklit'],
    '427-347 v. Chr.': ['Platon'],
    '384-322 v. Chr.': ['Aristoteles'],
    '341-271 v.Chr.':'[Epikur]',
    '1348': ['Autrecout'],
    '1822-1888': ['Rudolf Julius Clausius'],
    '1831-1879': ['James Clerk Maxwell'],
    '1844-1906': ['Ludwig Boltzmann']
}

while dicA:
    frage(dicA)

print("Sie beherrschen den Abriss der historischen Entwicklung!")
