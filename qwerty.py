#ex1

def f(A, k=0):
    if k == len(A):
        return A
    if k == len(A) - 1:
        print(A[k], end="")
    else:
        print(A[k], end=",")
    f(A, k + 1)

input_multime = {1, 2, 3}
l = list (input_multime)
print("{", end="")
f(l)
print("}", end=" ")
print()

#ex2
def perechi(lista):
    if not lista:
        return set();
    else:
        primul_el = lista[0][0];
        coada = lista[1:];
        return {primul_el} | perechi(lista[1:]);


input_l = [(1,2),(3,4)]
print(perechi(input_l))

#ex3
import functools
def my_filter(f,A,B=set()):       
    def func( acc, el ):
        if(f(el)):
            B.add(el);
        return f(el);
    functools.reduce(func,A,0);
    return B;

input_l = {1, 2, 3, 4};
B = set(my_filter(lambda x : x % 2 == 0,input_l));

print( B );

#ex4
def standard ( f, s, A = set(), B = set() ):
    if not s:
       return  A, B;
    primul = s.pop()
    rest = s;
    if ( f( primul) ):
        A.add(primul);
    else:
        B.add(primul);
    return standard(f,rest,A,B)

print(standard(lambda x : x % 2 == 0, {1,2,3,4}))
    
#ex5
def r_i( lista_multime ):
    reuniune = set().union(*lista_multime);
    intersectie = set.intersection(*lista_multime);

    return reuniune, intersectie;

k = [{1,2,3}, {1,2,3,4}, {3,5,6,7}]

print(r_i(k))   

#ex6
def cifra ( numar ):
    if ( numar == 0 ) :
        return set();
    else:
        return {numar%10} | cifra ( numar // 10 );

def const(numere):
    if not numere:
        return []
    else:
        return [cifra(numere[0])] + const(numere[1:])
        
def reuniune( A ):
    if len(A) == 1:
        return A[0];
    else:
        return A[0] | reuniune(A[1:]);

def intersectie( A ):
    if len(A) == 1:
        return A[0];
    else:
        return A[0] & intersectie(A[1:]);

p = {1234, 123, 127}
m = const(list(p))
print(reuniune(m))
print(intersectie(m));

#Dictionare

#ex1
def suma( lista, d={}):
    if not lista:
        return d;
    if ( lista[0][0] in d) :
        d[lista[0][0]] = lista [0][1] + d[lista[0][0]];
    else:
        d[lista[0][0]] = lista[0][1];

    return suma(lista[1:], d )

i = [('a', 7), ('b', 5), ('c', 2), ('a', 3), ('b', 3)]

print( suma ( i ) )

#ex2

def ap( l , k = 0, r = 0):
    if not r:
        r = {};
    if k == len(l):
        return r;

    sir = l[k];
    def formare(sir, caracter = 0):
        if caracter < len (sir):
            c = sir [caracter];
            if c in r:
                r[c] += 1;
            else:
                r[c] = 1;

            formare(sir, caracter + 1 );
    formare(sir);

    return ap( l, k + 1, r)

i = ["aaa", "bbb", "aabbb"]
print ( ap ( i ) )

#ex3
def fil ( d, k ):
    if not d:
        return {}
    cheie , valoare = d.popitem()
    if k(cheie, valoare):
        m  = fil(d,k);
        m[cheie] = valoare;
        return m;
    else:
        return fil(d, k )
        

def cond ( cheie, valoare ):
    return valoare >= 5;

d = {'a': 5, 'b': 7, 'c': 1}
print ( fil ( d.copy(), cond ) )

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
print ( f" exists: {e}, for_all: {t}")

