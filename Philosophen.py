from random import choice

def frage(d):
    a = choice(list(d.keys()))
    print("Um welchen Philosophen assoziiert man durch folgende Charakterisierung:", a, "?")
    aw = input("Es handelt sich um den Philosophen: ")
    if aw not in d[a]:
        print("Falsch!")
        print("Es handelt sich um den Philosophen" ', '.join(d[a]))
    else:
        print("Richtig!")
        del d[a]

# Dictionary
dicA = {
    'Vorsokratiker, jüngerer Zeitgenosse des Sokrates,\n' 
    'wurde jedoch nicht von ihm beeinflusst. Schüler von\n'
    'Leukipp. Er beeinflusste den hellenistischen Philosoph\n'
    'Epikur Hauptvertreter der antiken Atomistik. Zentrale \n'
    'Aussage: Nur scheinbar hat ein Ding eine Farbe, nur \n'
    'scheinbar ist es süß oder bitter, in Wirklichkeit gibt \n'
    'nur Atome im Leeren Raum': ['Demokrit'],
    'Befasste sich mit der Frage der Weltentstehung (Kosmogonie).\n'
    'Er versuchte die Ordnung und Beschaffenheit des Weltalls zu\n' 
    'klären. Er führte die Lehre von den vier Urstoffen (Elementen) \n'
    'ein': ['Empedokles'],
    'Verfasste ein einziges kurzes Werk mit dem Titel: Über die Natur.\n'
    'Die Botschaft, die aus seinem Werk hervorgeht manifestiert sich in \n'
    'Sprichwort: Ex nihilo nihil (Aus Nichts wird Nichts)': ['Parmenides'],
    'Vorsokratischer Philosoph. Begriff des Logos, der die vernunftgemäße\n'
    'Weltordnung und ihre Erkentnis und Erklärung bezeichnet, der natürliche\n'
    'Prozess beständigen Werdens und Wandelns, deren Bergriff in späterer Zeit\n'
    'in die kurformel: panta rhei (Alles fließt) gebracht wird.':['Heraklit'],
    'Schüler des Sokrates. Er setzt Maßstäbe in der Metaphysik, Erkenntnistheorie,\n'
    'Ethik, Anthropologie, Staatstheorie, Kosmologie, Kunsttheorie und Sprachphilosophie.\n'
    'Griff die Hypothese der vier Grundelemente wieder auf, denen er reguläre geometrische\n'
    'Körper zuordnet. Feuer: Tetraeder, Luft: Oktaeder, Wasser: Ikosaeder, Erde: Würfel': ['Platon'],
    'Lehnt Atomismus im Wesentlichen ab. Er glaubt nicht an die Existenz des \n'
    'leeren Raumes zwischen den Atomen': ['Aristoteles'],
    'Neben der räumlichen Ausdehnung wird den Atomen auch eine Schwere zugeschrieben':['Epikur'],
    'Widerstand der Kirche zwang seine entwickelte Atomtheorie in den Widerruf': ['Autrecout'],
    'Gemeinsame Entwicklung der kinetischen Gastheorie; Zurückführung der \n'
    'makroskopischen Eigenschaften der Gase wie Druck, Temperatur oder spez.\n'
    'Wärme auf Atome, die verschiedene kinetische Energien haben und untereinander\n'
    'durch Stöße Wechselwirken.': ['Rudolf Julius Clausius','James Clerk Maxwell','Ludwig Boltzmann']
}

while dicA:
    frage(dicA)

print("Sie beherrschen den Abriss der historischen Entwicklung!")
