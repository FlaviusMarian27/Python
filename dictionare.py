#ex1

def suma ( l , d = {} ):
    if not l:
        return d

    if l[0][0] in d:
        d[l[0][0]] = l[0][1] + d[l[0][0]]
    else:
         d[l[0][0]] = l[0][1]

    return suma(l[1:], d)

m =  [('a', 7), ('b', 5), ('c', 2), ('a', 3), ('b', 3)]
print( suma( m ) )

#ex2

def ap ( l , k = 0 , r = 0 ):
    if not r:
        r = {}
    if k == len ( l ):
        return r;
    sir = l[k]
    def formare( sir, caracter = 0 ):
        if ( caracter < len(sir)):
            c = sir[caracter]
            if c in r:
                r [ c ] = r [ c ] + 1;
            else:
                r[ c ] = 1;
            formare(sir, caracter + 1 )

    formare(sir)

    return ap(l, k +1 , r)

i=[ "aaa" , "bbb", "aabbb" ]
print(ap(i))

#ex3

def fil( d , f ):
    if not d:
        return {}
    cheie, valoare = d.popitem()
    if f (cheie, valoare):
        m = fil(d,f)
        m[cheie] = valoare;
        return m;
    else:
        return fil(d,f)
    
def cond(cheie , valoare):
    if ( valoare >= 5 ):
        return valoare
di = {'a': 5, 'b': 7, 'c': 1}

print(fil(di,cond))

#ex4

from functools import reduce

def exists(conditie, dictionar):
    return reduce(lambda acc, elem: acc or conditie(elem[0], elem[1]), dictionar.items(), False)

def for_all(conditie, dictionar):
    return reduce(lambda acc, elem: acc and conditie(elem[0], elem[1]), dictionar.items(), True)

di = {'a': 5, 'b': 7, 'c': 1}

conditie = lambda cheie, valoare: valoare >= 5

exists_result = exists(conditie, di)
for_all_result = for_all(conditie, di)

print(f"exists: {exists_result}, for_all: {for_all_result}")
