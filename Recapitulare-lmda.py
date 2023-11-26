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

#1  lista nodurilor care au un singur fiu
def srd(tree):
    if(tree == None):
        return [];
    if((tree["left"] != None and tree["right"]== None) or (tree["left"] == None and tree["right"] != None)):
       return srd(tree["left"]) + [tree["value"]] + srd(tree["right"])
    return srd(tree["left"]) + srd(tree["right"])
                                                    
print(srd(bt))

#nodurile care au 2 copii

def fii(tree):
    if tree is None:
        return []
    if tree["left"] is not None and tree["right"] is not None:
        return [tree["value"]] + fii(tree["left"]) + fii(tree["right"]) 
    return fii(tree["left"]) + fii(tree["right"])

print(fii(bt))


#noduri care sunt frunze dar varianta ca la 1 sau 2 fii

def fr(tree):
    if tree is None:
        return []
    if tree["left"] is  None and tree["right"] is  None:
        return [tree["value"]] + fr(tree["left"]) + fr(tree["right"]) 
    return fr(tree["left"]) + fr(tree["right"])

print(fr(bt))

# lista frunzelor
def frunze( tree , l = [] ):
    if tree["left"] == None and tree["right"] == None :
        l = l + [ tree ["value"] ]
    else:
        if tree["left"] != None:
            l = frunze(tree["left"],l)
            
        if tree["right"] != None:
            l = frunze(tree["right"],l)
    return l;

print(frunze(bt))

#2 numărul total de noduri din arbore
def nr(tree):
    if tree == None:
        return 0;
    else:
        if "left" in tree:
            l = nr(tree["left"])
        else:
            return 0;
        if "right" in tree:
            r = nr(tree["right"])
        else:
            return 0
        return 1 + l + r;
 

p = nr(bt)
print(p)


#PREORDINE
def pre(tree):
    if tree is None:
        return []
    return [tree["value"]] + pre(tree["left"]) + pre ( tree [ "right" ] );


print(pre(bt))

#INORDINE
def ino(tree):
    if tree is None:
        return [];
    return ino(tree["left"]) + [tree["value"]] + ino(tree["right"]);

print(ino(bt))

#POSTORDINE

def pos(tree):
    if tree is None:
        return []
    return pos(tree["left"]) + pos(tree["right"]) + [tree["value"]];
print(pos(bt))

#nod par
def par( tree ):
    if tree is None :
        return;
    par(tree["left"])
    par(tree["right"])
    if tree["value"] % 2 == 0 :
        print(tree["value"])

par(bt)

#returnare lista

def p_h(tree,p = []):
    if tree is None:
        return [];
    p_h(tree["left"],p)
    p_h(tree["right"],p)
    if tree["value"] % 2 == 0:
        p.append(tree["value"]);

    return p
l = p_h(bt)
print(l)

#nod impar
def par( tree ):
    if tree is None :
        return;
    par(tree["left"])
    par(tree["right"])
    if tree["value"] % 2 == 1 :
        print(tree["value"])

par(bt)

#returnare lista imp

def i_h(tree,i = []):
    if tree is None:
        return [];
    i_h(tree["left"],i)
    i_h(tree["right"],i)
    if tree["value"] % 2 == 1:
        i.append(tree["value"]);

    return i
l = i_h(bt)
print(l)

