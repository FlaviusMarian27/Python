#Liste

#elementele pare afisate
def pare(l, k= 0):
    if k >= len(l):
        return k;
    if l[k] % 2 == 0:
        print(l[k])
    pare(l,k+1)

lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pare(lis)


#elementele care au mai putin de trei caractere

def trei( l , k = 0,p=[] ):
    if k >= len(l):
        return k;
    if len(l[k]) > 3:
        p.append(l[k])
    trei(l,k+1)
    return p
lista = ["abee", "c", "def", "ghij"]
print(trei(lista))


#să se înmulțească toate elementele unei liste de numere reale
import functools

q = functools.reduce(lambda a,b: a * b , [1,2,3,4,5] )
print(q)

#varianta recursiva

def produs(l, k = 0):
    if k >= len(l):
        return 1;
    else:
        return l[k] * produs(l,k+1)
o = [1,2,3,4,5]
print(produs(o))

#suma tuturor
from functools import reduce

s = reduce(lambda a,b : a + b, [1,2,3,4,5])
print(s)

#suma
def suma(l,k = 0):
    if k>=len(l):
        return 0;
    else:
        return l[k] + suma(l,k+1)

o = [1,2,3,4,5]
print(suma(o))

#map cu x**3

t = list(map(lambda x : x*x*x, [1,2,3,4,5]))
         
print ( t )
         
#filter pentru prime

def prim(n, d = 2):
    if ( n < 2 ):
        return False
    if ( n == 2 ):
        return True
    if ( n % d == 0):
        return False
    if (d*d > n):
        return True
    else:
        return prim(n,d+1);
    
primi = list(filter(prim, [1,2,3,4,5]))

print(primi)

#cifrele impare
def cifimp(n,l = []):
    if(n == 0):
        return l
    if (n%10)%2!=0:
        l.append(n%10);
    
    return cifimp(n // 10,l);

lista = 785965455
i = cifimp(lista);
print(i)

#cifrele pare
def cifp(n,l = []):
    if(n == 0):
        return l
    if (n%10)%2==0:
        l.append(n%10);
    
    return cifp(n // 10,l);

lista = 785965455
i = cifp(lista);
print(i)

def sapte(n,l = []):
    if(n == 0):
        return l
    if n%10 < 7:
        l.append(n%10);
    
    return sapte(n // 10,l);

lista = 785965455
s = sapte(lista);
print(s)

#suma elementelor pare din lista

def suma_par(l , k = 0 ):
    if k >= len(l):
        return 0;
    
    if l[k] % 2 == 0:
        return l[k] + suma_par(l,k+1)
    else:
        return suma_par(l,k+1)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(suma_par(lista))

#maximul par

def maximul(l, k = 0 , maxi = 0 ):
    if k >= len(l):
        return maxi;
    if l[k] % 2 == 0:
        if ( l[k] > maxi ):
            maxi = l[k];
        return maximul(l,k+1,maxi);
    
    return maximul(l,k+1,maxi);
lista = [1, 2, 3, 4, 5, 6, 700, 8, 9, 10, 80]
rezultat = maximul(lista)
print(rezultat)

print(" ")




#MULTIMI

#ex1

def afisare(a,k=0):
    if k >= len(a):
        return k
    if k == len(a) - 1 :
        print(a[k], end="")
    else:
        print(a[k], end=",")
    afisare(a,k+1)

m={1,2,3}
l = list(m)
print("{", end="")
afisare(l)
print("}", end=" ")
print()

#2
def lista ( l ):
    if not l :
        return set()
    if l :
        return {l[0][0]} | lista(l[1:])

m = [ (1,2) , (3,4) ]
print(lista(m))

#3

def fil(f,a,b=set()):
    def func(acc,elem):
        if f(elem):
            b.add(elem)
        return f(elem)
    return b

def par(x):
    if x % 2 == 0:
        return x;

b = set(filter(par,{1,2,3,4}))
print(b)

#4
def partition(f,s,a=set(),b=set()):
    if not s:
        return a,b
    p = s.pop()
    if f(p):
        a.add(p)
    else:
        b.add(p)
    return partition(f,s,a,b)

m={1,2,3,4}
x = partition( lambda x : x % 2 == 0, m )
print(x)

#5
def rsi(l,k = 0 ):
    if k >= len(l):
        return set(), set()
    r,i = rsi(l,k+1)

    r = r.union(l[k])
    if i:
        i = i.intersection(l[k])

    else:

        i = l[k]

    return r,i

print(rsi ( [{1, 2, 3}, {1, 2, 3, 4}, {3, 5, 6, 7}] ))

#5.2
def c(l):
    r = set().union(*l)
    i = set.intersection(*l)

    return r,i

print(c ( [{1, 2, 3}, {1, 2, 3, 4}, {3, 5, 6, 7}] ))

#6
def cifra( n ):
    if not n :
        return set()
    else:
        return {n%10} | cifra(n//10)

def const(numere):
    if not numere:
        return []
    else:
        return [cifra(numere[0])] + const(numere[1:])

def reuniune (a):
    if len(a) == 1:
        return a[0]
    else:
        return a[0] | reuniune(a[1:])

def intersectie (a):
    if len(a) == 1:
        return a[0]
    else:
        return a[0] & intersectie(a[1:])

p = {1234, 123, 127}
m = const(list( p ))
print ( reuniune ( m ) , intersectie ( m ) )

print(" ")

#DICTIONARE

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

        


#ARBORI
    
print(" ")
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

#preordine
def rsd(tree):
    if tree == None:
        return []
    return [tree["value"]] + rsd(tree["left"]) + rsd(tree["right"])

print(rsd(bt))

#inordine
def srd(tree):
    if tree == None:
        return []
    return srd(tree["left"])+[tree["value"]]+srd(tree["right"])

print ( srd ( bt ) )

#postordine
def sdr(tree):
    if tree == None:
        return []
    return sdr(tree["left"])+sdr(tree["right"])+[tree["value"]]

print ( sdr ( bt ) )


#1  lista nodurilor care au un singur fiu

def fiu(tree):
    if (tree == None):
        return []
    if ((tree["left"] == None and tree["right"] != None) or (tree["left"] != None and tree["right"] == None)):
        return fiu(tree["left"])+[tree["value"]]+fiu(tree["right"])

    return fiu(tree["left"])+fiu(tree["right"])

print ( fiu ( bt ) )


#nodurile care au 2 copii
def fiu2(tree):
    if (tree == None):
        return []
    if (tree["left"] != None and tree["right"] != None):
        return fiu2(tree["left"])+[tree["value"]]+fiu2(tree["right"])

    return fiu2(tree["left"])+fiu2(tree["right"])

print ( fiu2 ( bt ) )

#noduri care sunt frunze

def frunze(tree):
    if (tree == None):
        return []
    if (tree["left"] == None and tree["right"] == None):
        return frunze(tree["left"])+[tree["value"]]+frunze(tree["right"])

    return frunze(tree["left"])+frunze(tree["right"])

print ( frunze ( bt ) )

#2 numărul total de noduri din arbore

def nr ( tree ) :
    if tree == None:
        return 0;
    else:
        if "left" in tree:
            l = nr(tree["left"])
        if "right" in tree:
            r = nr(tree["right"])
        else:
            return 0;
        z = 1+ r + l
        return z;
p =nr(bt)
print(p)

#nod par

def par( tree ):
    if tree == None:
        return ;
    par(tree["left"])
    par(tree["right"])
    if tree["value"]%2== 0:
        print(tree["value"])

par(bt)

#nod par lista

def par_l(tree, p = [] ):
    if tree == None:
        return p;
    par_l(tree["left"],p)
    par_l(tree["right"],p)

    if tree["value"]%2==0:
        p.append(tree["value"])

    return p;

print(par_l(bt))


#nod impar

def impar( tree ):
    if tree == None:
        return ;
    impar(tree["left"])
    impar(tree["right"])
    if tree["value"]%2== 1:
        print(tree["value"])

impar(bt)

#nod impar lista

def impar_l(tree, p = [] ):
    if tree == None:
        return p;
    impar_l(tree["left"],p)
    impar_l(tree["right"],p)

    if tree["value"]%2==1:
        p.append(tree["value"])

    return p;

print(impar_l(bt))
