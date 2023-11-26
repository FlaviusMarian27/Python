#diferenta -
#unire |
#intersectie &
#diferenta_simetrica ^

#ex1

def tiparire( A, k = 0 ):
    if ( k >= len(A) ):
        return A
    if ( k == len(A) - 1 ):
        print(A[k],end="");
    else:
        print(A[k],end=",")
    tiparire(A,k + 1)

m = {1,2,3}

l = list( m )
print("{", end="")
tiparire(l)
print("}", end=" ")
print()

#ex2
def lista( l ):
    if not l :
        return set()
    
    if l:
        primul = l[0][0];
        coada = l[1:];
        return {primul} | lista(coada);

m = [ (1,2),(3,4) ]
print(lista(m))

#ex3

from functools import reduce

def my_filter(f, A, B=set()) :
    def functie(acc, elem):
        if ( f ( elem ) ):
            B.add(elem);
        return f(elem);
    reduce(functie,A,0);
    return B;
b = set(my_filter(lambda x : x % 2 == 0, {1,2,3,4}))
print(b)

#ex4
def partition ( f, s, A=set(), B=set() ):
    if not s:
        return A,B

    primul = s.pop();
    restul = s;
    if ( f ( primul ) ):
        A.add(primul);
    else:
        B.add(primul);
    return partition(f,restul,A,B)

print(partition(lambda x: x % 2 == 0 , {1,2,3,4}))

#ex5
def rsiu(l):
    reuniune = set().union(*l)
    intersectie = set.intersection(*l);
    return reuniune, intersectie;

print( rsiu ( [ {1,2,3}, {1,2,3,4}, {3,5,6,7} ] ))


#ex5.1
def rsiu2( lis, k = 0):
    if k >= len ( lis ) :
        return set()
    reuniune, intersectie = rsiu2(lis, k + 1)
     

    reuniune = reuniune.union(lis[k])
    intersectie = intersectie.intersection(lis[k])

    return reuniune, intersectie

print( rsiu2 ( [{1, 2, 3}, {1, 2, 3, 4}, {3, 5, 6, 7}] ) )

#ex6
def cifra ( n ):
    if not n :
        return set()
    else:
        return { n % 10 } | cifra( n // 10 )

def const ( numere ):
    if not numere:
        return []
    else:
        return [cifra(numere[0])] + const(numere[1:])

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
print ( reuniune ( m ) )
print ( intersectie ( m ) )

'''
AFISARE

{1,2,3} 
{1, 3}
{2, 4}
({2, 4}, {1, 3})
({1, 2, 3, 4, 5, 6, 7}, {3})
({1, 2, 3, 4, 5, 6, 7}, {3})
{1, 2, 3, 4, 7}
{1, 2}

'''
