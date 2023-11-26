#ex1
def suma ( l, d = {} ):
    if not l:
        return d;
    if l[0][0] in d :
        d [ l [0] [0] ] = l [0] [1] + d [ l [0][0]  ];
    else:
        d [ l [0] [0] ] = l [0] [1];
    return suma(l[1:],d)
m = [('a', 7), ('b', 5), ('c', 2), ('a', 3), ('b', 3)]
print ( suma ( m ) );

#ex2
def ap( l , k = 0, r = 0):
    if not r:
        r = {};
    if k == len ( l ) :
        return r
    sir = l [ k ]
    def formare(sir, caracter = 0):
        if caracter < len (sir):
            c = sir [caracter];
            if c in r:
                r [ c ] = r [ c ] + 1;
            else:
                r [ c ] = 1;

            formare(sir, caracter + 1 );
    formare(sir);
    return ap( l, k + 1, r)
i = ["aaa", "bbb", "aabbb"]
print(ap(i))

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
print ( f"exists: {e}, for_all: {t}")

#ex5
from functools import reduce

i = {'a': 5, 'b': 7, 'c': 6}
f = lambda x: x + 1

o = reduce(lambda acc, item: (acc.update({item[0]: f(item[1])}), acc)[1], i.items(), {})

print(o)



#ex6
def f( d, stri_lis, k = 0, result = 0 ):
    if not result:
        result = set()

    if k < len ( stri_lis ):
        curent_stri = stri_lis[k]
        if curent_stri in d:
            result.add(d[curent_stri])
        return f(d,stri_lis, k + 1, result)
    return result

input_d = {'aa': 5, 'bb': 7, 'ca': 6}
input_list = ['aa', 'bb', 'c']

r = f ( input_d, input_list )
print(r)


#ex7

def maximul ( f, d, maxi = 0 ):
    if not d:
        return maxi
    key, value = d.popitem()
    r = f(key,value)

    if r > maxi:
        maxi = r

    return maximul ( f, d, maxi)

def dublu ( key, value ):
    return value * 2

i = {'a': 5, 'b': 7, 'c': 6}

r = maximul ( dublu , i )
print ( r ) 


