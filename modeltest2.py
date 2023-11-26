#1
def intersectie(l1,l2):
    set1=set(l1)
    set2=set(l2)
    i = set1.intersection(set2)

    return i

lis1 = [1,7,8,10]
lis2 = [3,4,7,8]

print(intersectie(lis1,lis2))

#2

def cheie(di1,di2):
    s1 = set(di1.keys())
    s2 = set(di2.keys())

    i = s1.intersection(s2)

    return i

d1 = {1: 0, 18 : 1, 118: 2}
d2 = {3: 1, 1: 3, 118: 4}

print(cheie(d1,d2))


#3

def frunze(tree):
    if tree is None:
        return []
    if (tree["left"] == None and tree["right"] == None ) or (tree["left"] == None and tree["right"] == None):
        return frunze(tree["left"]) + [tree["value"]] + frunze(tree["right"])
    return frunze(tree["left"]) + frunze(tree["right"])


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

print(frunze(bt))

        
