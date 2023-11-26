#PARTEA I 

#1.1
def par(lista,k=0):
    if(k>=len(lista)):
        return lista
    
    if( lista[k]%2==0):
        print(lista[k])
        
    return par(lista, k+1)

lista=[1,2,3,4,5,66,78,9]
par(lista)

#1.2
r= list(filter(lambda x: x % 2 == 0, [1,2,3,45,88,7,6,89,8]))
print(r)
#2
def trei(lista, k = 0):
    if( k >= len(lista) ):
        return lista;

    if( len(lista[k]) < 3 ):
        print(lista[k]);

    return trei(lista, k + 1 );

lista = ["ab", "c", "def", "ghij"]
trei(lista)

#3
l = ( 1 , 45,  6, 7, 5,8,9);
x=sorted(l);
print(x)

#4
def cifra(n):
    return n % 10;

def sortare(lista):
    return sorted(lista,key = cifra);

lista = [123, 456, 789, 321];
print(sortare(lista))

#5.1
import functools
p = functools.reduce(lambda a,b: a * b, [1,2,3,4,5])
print(p )

#5.2
from functools import reduce
def produs(lista, k = 0):
    if  ( k >= len(lista)):
        return 1;
    return lista[k] * produs(lista, k + 1);

lista = [1,2,3,4,5];
r = produs(lista);
print(r);

#6.1
lista_nr1 = [1,2,3,4,5];
puterea_3 = list(map(lambda x : x ** 3, lista_nr1))

print(puterea_3)

#6.2

def p3(lista):
    if( len(lista)== 0):
        return lista;
    return [lista[0]**3] + p3(lista[1:])

l1= [1,2,3,4,5];
p= p3(l1)
print (p)

#7
def pri(n):
    if ( n < 2 ):
        return False;
    for i in range (2, int(n**0.5) + 1 ):
        if( n % i == 0 ):
            return False;
    return True;
lista_initiala = [1,2,3,4,5,6,7,8,9,10];

p = list(filter(pri, lista_initiala));
print ( p )
    
#PARTEA II

#1
#A
def cif_imp(n):
    c = [];
    while ( n > 0 ):
        cifra = n % 10;
        if ( cifra % 2 != 0 ):
            c.append(cifra);
        n = n // 10;
    return c;
    
lista = 785965455
i = cif_imp(lista);
print(i)

def cif_par(n):
    c = [];
    while ( n != 0 ):
        if( (n % 10)%2 == 0 ):
            c.append(n%10);
        n = n // 10;
    return c;

lista = 785965455
par = cif_par(lista);
print(par)

def sub7(n):
    c = [];
    while( n > 0 ):
        if(n%10 < 7):
            c.append(n%10);
        n = n // 10;
    return c;

lista = 785965455
m7 = sub7(lista);
print(m7)

def ordine(n):
    l = [];
    while( n > 0 ):
        l.append(n%10);
        n = n // 10;
    return sorted(l);
    
lista = 785965455
o = ordine(lista);
print(o)

def inv(n):
    l = [];
    while( n > 0 ):
        l.append(n%10);
        n = n // 10;
    return sorted(l, reverse = True);
    
lista = 785965455
inv = inv(lista);
print(inv)

#B
def cond(n, k):
    l = []
    while n > 0:
        if k(n % 10):
            l.append(n % 10)
        n = n // 10
    return l

def este_impara(cifra):
    return cifra % 2 != 0

n = 78595455
lis = cond(n, este_impara)
print(lis)

#C

def direct (c,k):
    nr = 0;
    for cifra in c:
        if( k(cifra)):
            nr = nr * 10 + cifra;
    return nr;

cifre = [1,2,3,4,5,6,7,8,9];

def imp(cif):
    return cif % 2 != 0;

r = direct(cifre, imp);
print(r);

from functools import reduce
def filt(c, k):
    cf=filter(k,c);
    return reduce(lambda acc, c: acc * 10 + c, cf, 0);
cifre = [1,2,3,4,5,6,7,8,9];

def este_impa(cifra):
    return cifra % 2 != 0;
r = filt( cifre, este_impa);
print(r);

#2

def div(a,b,d):
    l=[];
    for i in range (b, a-1, -1):
        if( i % d == 0 ):
            l.append(i);
    return l;


div = div(10, 30, 3)
print(div)

#3
#a
def nth ( l, n ):
    if ( n >= len (l) ):
        return None;
    return l[n];

#b
def firstn(l, n):
    return l[:n];

l_ex = [1,2,3,4,5,6,7,8,9];
n_ele = nth(l_ex, 8 );
print(n_ele);

pr= firstn(l_ex,3);
print(pr);

#Parcugeri de liste

#5
#A.1
from functools import reduce

def filter1(k,l):
    return reduce(lambda nr, i: nr + [i] if (k(i)) else nr, lista, []);
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def este_par(numar):
    return numar % 2 == 0
rezultat = filter1(este_par, lista)
print(rezultat)

#A.2

def filter_personalizat(conditie, lista):
    rezultat = []
    for element in lista:
        if conditie(element):
            rezultat.append(element)
    return rezultat

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def este_par(numar):
    return numar % 2 == 0

rezultat = filter_personalizat(este_par, lista)
print(rezultat)

#B

def exists ( lista, k ):
    if ( len(lista) == 0 ):
        return False
    elif( k ( lista[0] )):
        return True
    return exists(lista[1:], k);

def maimare( n ):
    return n > 10;

l = [ 5, 8, 12, 15, 3 ]

if ( exists( l, maimare) != 0):
    print(  "Avem nr mai mari decat 10");
else:
    print ( "Nu avem numerre mai mari decat 10");

#6
#A
from functools import reduce

def countif ( f, lista ):
    return reduce(lambda acc, el : acc + f( el ), lista, 0 )

def par(n):
    return n% 2 == 0;

l = [ 1,2,3,4,5,6,7,8,9,10]
print ( countif( par, l ))

#B
from functools import reduce

def sumif(f, lista):
    return reduce(lambda acc, el: acc + el if f(el) else acc, lista, 0)


def este_par(num):
    return num % 2 == 0

numere = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

rezultat = sumif(este_par, numere)
print(rezultat)

#7
def split(p):
    if len(p) == 0:
        return [], []

    if isinstance(p[0], tuple):
        lista_1 = [p[0][0]] + split(p[1:])[0]
        lista_2 = [p[0][1]] + split(p[1:])[1]
    else:
        lista_1 = [p[0]] + split(p[1:])[0]
        lista_2 = [None] + split(p[1:])[1]

    return lista_1, lista_2

def combine(lista_1, lista_2):
    if not lista_1 or not lista_2:
        return []

    if lista_2[0] is not None:
        p = (lista_1[0], lista_2[0])
    else:
        p = lista_1[0]

    return [p] + combine(lista_1[1:], lista_2[1:])

p = [(1, 2), (3, 4), 5, 6]

rezultat_split = split(p)
print(rezultat_split)  

rezultat_combine = combine(rezultat_split[0], rezultat_split[1])
print(rezultat_combine)

#9
def num( c ):
    if not c:
        return 0;
    else:
        return c[-1] + num(c [:-1] ) *10

l = [1,2,3,4];
print (num(l))
    
#11
def comparare(l1,l2):
    if len(l1) < len(l2):
        return -1;
    elif len(l1) > len(l2):
        return 1;
    else:
        for i in range (len(l1)):
            if ( l1[i] != l2[i] ):
                return l1[i] - l2[i];
    return 0;

print(comparare([1, 2, 3], [1, 2, 3, 4]))  #  -1
print(comparare([1, 2, 3, 4], [1, 2, 3]))  #  1
print(comparare([1, 2, 3], [1, 2, 3]))     #  0
print(comparare([1, 2, 3], [1, 2, 4]))     #  -1
print(comparare([1, 2, 4], [1, 2, 3]))      #1

'''
rezultate
2
4
66
78
[2, 88, 6, 8]
ab
c
[1, 5, 6, 7, 8, 9, 45]
[321, 123, 456, 789]
120
120
[1, 8, 27, 64, 125]
[1, 8, 27, 64, 125]
[2, 3, 5, 7]
[5, 5, 5, 9, 5, 7]
[4, 6, 8]
[5, 5, 4, 5, 6, 5]
[4, 5, 5, 5, 5, 6, 7, 8, 9]
[9, 8, 7, 6, 5, 5, 5, 5, 4]
[5, 5, 5, 9, 5, 7]
13579
13579
[30, 27, 24, 21, 18, 15, 12]
9
[1, 2, 3]
[2, 4, 6, 8]
[2, 4, 6, 8]
Avem nr mai mari decat 10
5
30
([1, 3, 5, 6], [2, 4, None, None])
[(1, 2), (3, 4), 5, 6]
1234
-1
1
0
-1
1
'''
