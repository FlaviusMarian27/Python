
#ex1
def element(a,b,c):
    m = max(a,b,c);
    n = min(a,b,c);
    return  n , m;

print(element(5,7,2)) 

#ex2
def f(y):
    return conditie(y)

def conditie( x ):
    if( x > 25 ):
        return "Conditie indeplinita";
    else: 
        return "eroare";

print(f(56))

#ex3
def suma(lista, k=0, s=0):
    if k >= len(lista):
        return s

    if lista[k] % 5 == 0:
        s = s + lista[k]

    return suma(lista, k + 1 , s)

l = [4, 10, 4, 5, 9, 25, 12, 2]
print(suma(l))

