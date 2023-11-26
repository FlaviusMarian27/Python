'''# Crearea și afișarea unui graf in PYTHON:
graf = {
   "a" : {"b","c"},
   "b" : {"a", "d"},
   "c" : {"a", "d"},
   "d" : {"e"},
   "e" : {"d"}
}

print(graf)

# Afișarea nodurilor unui graf
graf = {
   "a" : {"b","c"},
   "b" : {"a", "d"},
   "c" : {"a", "d"},
   "d" : {"e"},
   "e" : {"d"}
}

def afisare_noduri(graf):
    return list(graf.keys())

print(afisare_noduri(graf))

# Afișarea muchiilor unui graf
graf = {
   "a" : {"b","c"},
   "b" : {"a", "d"},
   "c" : {"a", "d"},
   "d" : {"e"},
   "e" : {"d"}
}

import functools

def afisare_muchii(graf, muchii = set()):
    def functie(acc,elem):
        cheie, valoare = elem
        def f_multime(acc2,elem2):
            muchii.add((cheie,elem2))
        functools.reduce(f_multime, valoare, 0)
    functools.reduce(functie, graf.items(), 0)
    return muchii

print(afisare_muchii(graf))


#1. Fie un graf reprezentat de mulțimea perechilor de noduri adiacente.
# Să se creeze structura de date care reține informațiile despre graf într-un dicționar.

import functools

def constructie_graf(multime, dictionar = {}):
    def functie(acc, elem):
        if (elem[0] in dictionar):
            dictionar[elem[0]].add(elem[1])
        else:
            dictionar[elem[0]] = set({elem[1]})
        if(not elem[1] in dictionar):
            dictionar[elem[1]] = set()
    functools.reduce(functie, multime, 0)
    return dictionar

print(constructie_graf({(1, 3), (1, 2), (2, 4), (4, 1)}))

'''
bt = { "value" : 2, "left":
            {
                "value": 7, "left": None, "right":
                {
                    "value": 6, "left":
                    {
                        "value": 5, "left": None, "right": None
                    }, "right":
                    {
                        "value":11, "left": None, "right": None
                    },
                },
            }, "right":
                {
                    "value": 4, "left": None, "right": None
                }
        }

def rsd(tree):
    if tree == None:
        return [];
    return [tree["value"]] + rsd(tree["left"]) + rsd(tree["right"])

print(rsd(bt))

#postordine
def sdr(tree):
    if ( tree==None):
        return;
    sdr(tree["left"]);
    sdr(tree["right"]);
    print(tree["value"]);
sdr(bt);
print(" ")
#celepare
def sdr(tree):
    if ( tree==None):
        return;
    sdr(tree["left"]);
    sdr(tree["right"]);
    if tree["value"] %2 == 0:
        print(tree["value"]);
sdr(bt);
