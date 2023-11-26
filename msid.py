#ex1
def suma(l,d={}):
    if not l :
        return d

    if l[0][0] in d:
        d[l[0][0]] = d[l[0][0]] + l[0][1]
    else:
        d[l[0][0]] = l[0][1]

    return suma(l[1:],d)

m = [('a', 7), ('b', 5), ('c', 2), ('a', 3), ('b', 3)]
print(suma(m))

#ex2
def ap ( l , k = 0 , r = 0 ):
    if not r :
        r = {}

    if k == len ( l ) :
        return r;

    s = l[k]
    def formare ( s, car = 0 ):
        if car < len(s):
            c = s[car]
            if c in r:
                r[c] = r[c] +1;
            else:
                r[c] =1;
            formare(s, car+1)

    formare(s)

    return ap(l,k+1,r)

i = ["aaa", "bbb", "aabbb"]
print(ap(i))

#ex3
def f (d,k):
    if not d:
        return {}
    c,v=d.popitem()

    if k(c,v):
        m = f(d,k)
        m[c] = v
        return m
    else:
        return f(d,k)

def cond ( c,v ):
    if v >= 5:
        return v;

d = {'a': 5, 'b': 7, 'c': 1}
print ( f ( d, cond ) )  

#ex4
from functools import reduce

def ex(c, d):
    def v(pereche):
        cheie, valoare = pereche
        return c(cheie, valoare)

    return reduce(lambda acc, pereche: acc or v(pereche), d.items(), 0)

def al(c, d):
    def v(pereche):
        cheie, valoare = pereche
        return c(cheie, valoare)

    return reduce(lambda acc, pereche: acc and v(pereche), d.items(), 1)

def conditie ( cheie, valoare ):
    return valoare >= 5;

d = {'a': 5, 'b': 7, 'c': 1}
e = ex(conditie, d )
t = al( conditie,d)
print ( f"exists: {e}, for_all: {t}")


#5
from functools import reduce

i = {'a': 5, 'b': 7, 'c': 6}
f = lambda x: x + 1

o = reduce( lambda acc, elem :{**acc,elem[0]: f(elem[1])},i.items(),{})

print(o)

#6
def f ( d , l , k = 0 , r = 0 ):
    if not r :
        r = set()
    if k < len(l):
        if l[k] in d:
            r.add(d[l[k]])
        return f(d,l,k+1,r)

    return r

input_d = {'aa': 5, 'bb': 7, 'ca': 6}
input_list = ['aa', 'bb', 'c']

print(f(input_d, input_list))


#7
def maximul ( f , d , maxi = 0):
    if not d :
        return maxi
    c,v = d.popitem()

    if f(c,v) > maxi:
        maxi = f(c,v)
    return maximul(f,d,maxi)

def dublu ( c, v ):
    return v * 2

i = {'a': 5, 'b': 7, 'c': 6}

r = maximul ( dublu , i )
print ( r )

        
