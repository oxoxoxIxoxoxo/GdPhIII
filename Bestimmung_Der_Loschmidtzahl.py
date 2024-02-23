from random import choice

def frage(d):
    a = choice(list(d.keys()))
    print("Wie lautet die allgemeine", a, "?")
    aw = input("Die allgemeine {} lautet: ".format(a))
    if aw not in d[a]:
        print("Falsch!")
        print("Die allgemeine", a, "lautet:", ', '.join(d[a]))
    else:
        print("Richtig!")
        del d[a]

# Dictionary mit LaTeX-Gleichungen
dicA = {
    'Gasgleichung': ['p·V=N·k·T'],
    'Gaskonstante': ['R=N_A·k']
}

while dicA:
    frage(dicA)

print("Sie beherrschen die Bestimmung der Gaskonstante aus der Loschmidtzahl!")
