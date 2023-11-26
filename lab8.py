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


    
