#EXERCITII LABORATOR 
# Ex 1

def nr_vl_dis(a,b,c):
    if(  a == b == c ):
        print("Toate valorile sunt egale");
    elif (a == b or b==c or a==c):
        if( a==b ):
            print ( "Argumentul 1 si 2 sunt egale");
        elif b==c:
            print ("Argumentul 2 si 3 sunt egale");
        else:
            print ("Argumentul 1 si 3 sunt egale");
    else:
        print ("Argumentele sunt diferite");
print( nr_vl_dis(1,2,3));


#Ex 2
def mediana(a, b, c):
    m= a + b + c - max(a,b,c) - min(a,b,c);
    return m;
r = mediana ( 1, 2, 3);
print ( "Media este: ", r); 

#Ex 3
import operator
def op_cu_fun( op, f, g):
    def rezultat(x):
        return op ( f(x), g(x) );
    return rezultat;
def f(x):
    return x * 2;
def g(x):
    return x + 3;

op_add = op_cu_fun(operator.add, f, g)
op_sub = op_cu_fun(operator.sub, f, g)

rezultat_add = op_add(5)  
rezultat_sub = op_sub(5)  

print(rezultat_add)  
print(rezultat_sub) 

#4

def f(x):
    return ( lambda x : x + 15)(x);
print ( f (3) );

#EXERCITIUL BONUS 
#CODUL GRESIT
'''
======================
def f x:
    return x + 1
print(f(1))
======================
def f(x)
    return x + 1;
print(f(1))
======================
def f(x):
return x + 1;
print(f(1))
======================
def f(x):
    if (x == 0):
    return true;
    else:
    return false
print(f(1))
======================
def f(x):
    if (x == 0):
        return true
    else
        return false;
print(f(1))
======================
def f(x):
    if (x == 0)
        return True
    else
        return False;
print(f(1))
======================
def f(x):
    if x == 0:
        return True
    else
        return False;
print(f(1))
======================
def f(x):
    if x == 0:
        return True
   else:
        return False;
print(f(1))
======================
def 3f():
    print("Fast food");
======================
def (x):
    return x + 1
======================
def x:
    return x + 1
======================
def increment():
    return x + 1
print(increment())
======================
def increment x:
    return x + 1
print(increment(5))
======================
increment(x):
    return x + 1
print(increment(5))
======================
import math as m
math.floor(3)
======================
import math 
floor(3)
======================
def impartire(x, y):
    return x \ y;
print(f(1, 2))
======================
dof f(x):
    return x + 5
print(f(1, 2))
======================


#CODUL CORECTAT


======================
def f (x):
    return x + 1
print(f(1))
======================
def f(x):
    return x + 1;
print(f(1))
======================
def f(x):
    return x + 1;
print(f(1))
======================
def f(x):
    if (x == 0):
        return True;
    else:
        return False;
print(f(1))
======================
def f(x):
    if (x == 0):
        return True;
    else:
        return False;
print(f(1))
======================
def f(x):
    if (x == 0):
        return True;
    else:
        return False;
print(f(1))
======================
def f(x):
    if(x == 0):
        return True;
    else:
        return False;
print(f(1));
======================
def f(x):
    if (x == 0):
        return True
   else:
        return False;
print(f(1))
======================
def f3():
    print("Fast food");
======================
def f(x):
    return x + 1
======================
def f(x):
    return x + 1
======================
def increment(x):
    return x + 1
print(increment())
======================
def increment (x):
    return x + 1;
print(increment(5))
======================
def increment(x):
    return x + 1
print(increment(5))
======================
import math as m
    m.floor(3)
======================
import math 
    math.floor(3)
======================
def impartire(x, y):
    return x / y;
print(f(1, 2))
======================
dof f(x):
    return x + 5
print(f(1))
======================
'''
#Exercitii pentru saptamana 2 tema

#EXERCITIUL 1

def dreptunghi(L,l):
    return L*l;
def paralelipiped( L, l, h):
    ab=dreptunghi(L,l);
    al=2*(L*h+l*h);
    at=2*ab+al;
    return at;
print ( dreptunghi(4,6) );
print (paralelipiped( 4, 6, 8));


#EXERCITIUL 2
def eliminare(caracter, *p):
    nou=[];
    for sir in p:
        nou.append(sir.replace(caracter, ' ' ));
    r=''.join(nou);
    return r;
print (eliminare( 'a', 'banana', 'portocala', 'pepene' ));

#EXERCITIUL 3
def suma(n):
    cost= 2.75*n;
    red= round(cost * 0.05, 1);
    sumin= cost - red;
    return sumin, red;

print(suma(3));
    
'''
REZULTATE AFISARE

Argumentele sunt diferite
None
Media este:  2
18
2
18
24
208
b n n portoc l pepene
(7.85, 0.4)

'''

    
    
    
   
