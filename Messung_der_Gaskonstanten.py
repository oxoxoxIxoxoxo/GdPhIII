from random import choice

def frage(d):
    a = choice(list(d.keys()))
    print("Wie lautet", a, "?")
    aw = input(a, " {} lautet: ".format(a))
    if aw not in d[a]:
        print("Falsch!")
        print(a, "lautet:", ', '.join(d[a]))
    else:
        print("Richtig!")
        del d[a]

# Dictionary mit LaTeX-Gleichungen
dicA = {
    'die innere Energie der Stoffmenge von 1 mol': ['U=f*1/2*k*T','1/2*f*R*T'],
    'die Zahl der Freiheitsgrade': ['f'],
    'die molare spezifische Wärme':['C_V=dU/dT_V','1/2*f*R'],
    'die Relation aus der die Gaskonstante R in Abhängigkeit des spezifischen Drucks und der spezifischen Wärme':['R=C_p-C_V'],
    'der bis heute genaueste Wert von R, der durch die Messung der Schallgeschwindigkeit\n'
    'v_S in einem mit Argon gefüllten akkustischen Resonator ermittelt wurde':['R=(v_s^2*M/(K*T))','1/T*M/K*(f0/n*r_0)^2'],
    'der Ausdruck für die Schallgeschwindigkeit, der durch Messung von f0 der radialen akkustischen Eigenresonanzen des sphärischen Resonators bestimmt wurde':['v_s=f*lambda','f0*r_0/n']
}

while dicA:
    frage(dicA)

print("Sie beherrschen die Bestimmung aus der Gasgleichung!")
