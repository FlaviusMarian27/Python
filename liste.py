
#elementele pare afisate

def elpar(l, k = 0 ):
    if k >= len(l) :
        return k;
    if l[k] % 2 == 0 :
        print( l [ k ] );
    elpar(l,k + 1);

lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elpar(lis)

#elementele care au mai putin de trei caractere

def str(l, k = 0 ) :
    if k >= len(l) :
        return k;

    if len(l[k]) > 3 :
        print(l[k])

    str(l,k+1);

lista = ["ab", "c", "def", "ghij"]
str(lista)

#să se înmulțească toate elementele unei liste de numere reale

from functools import reduce

p = reduce(lambda a,b : a * b, [1,2,3,4,5])
print(p)

#varianta recursiva

def produs(l, k = 0 ) :
    if k >= len(l) :
        return 1;
    else:
        return l[k] * produs ( l, k + 1 )

lis = [1,2,3,4,5]
print(produs(lis))

#suma tuturor
from functools import reduce

s = reduce(lambda a,b : a + b, [1,2,3,4,5])
print(s)

#suma
def suma ( l, k = 0 ) :
    if k >= len(l):
        return 0;
    else:
        return l[k] + suma(l,k+1);

lis = [1,2,3,4,5]
print(suma(lis))

#map cu x**3

t = list(map(lambda x : x ** 3 , [1,2,3,4,5]))
print(t)

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
p = cifp(lista);
print(p)

#cifrele <7
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
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 80]
rezultat = maximul(lista)
print(rezultat)
