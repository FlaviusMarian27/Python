#parcurgere cu reduce

import functools

def parcurgere_simpla(multime):
    functools.reduce(lambda acc, element: print(element), multime, 0)

parcurgere_simpla({1, 2, 3, 4, 5})

print(" ")

#suma elementelor
import functools

def suma_multime_int(multime):
    return functools.reduce(lambda acc, element: acc + element, multime, 0)

print(suma_multime_int({1, 2, 3}))

#ex1

def afisare(A, k = 0 ):
    if k >= len(A) :
        return k;
    if ( k == len(A) - 1 ) :
        print(A[k],end="")
    else:
        print(A[k],end=",")
    afisare(A,k+1)

m={1,2,3}
l = list(m)
print("{", end="")
afisare(l)
print("}", end=" ")
print()

#ex2
def lista ( l ):
    if not l :
        return set();
    if l :
        primul =l[0][0]
        coada = l[1:]
        return {primul} | lista(coada);

m = [ (1,2),(3,4) ]
print(lista(m))

#ex3

from functools import reduce

def filter(f,a,b=set()):
    def func(acc,elem):
        if(f(elem)):
            b.add(elem)
        return f(elem)
    reduce(func,a,0);
    return b
def par(x):
    if x % 2 == 0:
        return x ;
b = set(filter(par,{1, 2, 3, 4}))
print(b)

#ex4

def partition ( f , s , a = set() , b = set() ):
    if not s :
        return a , b;
    primul = s.pop();
    r = s;
    if ( f (primul)):
        a.add(primul)
    else:
        b.add(primul)
    return partition(f,s,a,b);

m = {1,2,3,4}


x = partition( lambda x: x % 2 == 0,m)
print(x)

#ex5

def rsi(l, k = 0):
    if k >= len(l) :
        return set(), set()

    r, i = rsi(l,k+1)

    r = r.union(l[k])
    if i:
        i = i.intersection(l[k])
    else:
        i = l[k].copy()
    return r,i

e = ( rsi ( [{1, 2, 3}, {1, 2, 3, 4}, {3, 5, 6, 7}] ) )
print(e)


#ex6

def cif ( n ):
    if not n :
        return set();
    else:
        return {n % 10 } | cif(n//10)

def const ( numere ):
    if not numere :
        return []
    else:
        return[cif(numere[0])] + const(numere[1:])

def reuniune ( A ):
    if len ( A ) == 1:
        return A[0]
    else:
        return A[0] | reuniune(A[1:])

def intersectie ( A ):
    if len ( A ) == 1:
        return A[0]
    else:
        return A[0] & intersectie(A[1:])

p = {1234, 123, 127}
m = const ( list ( p ) )
print ( reuniune ( m ) , intersectie ( m ) )

