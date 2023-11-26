'''
#Probleme exemple
def factorial(n):
    if ( n==0 or n==1 ):
        return 1;
    return n*factorial(n-1);

print(factorial(4));

def suma(n):
    if( n <= 9 ):
        return n;
    else:
        return n % 10 + suma(n // 10);
print ( suma ( 12345 ) ); '''

#EX 1
def prog(n):
    if (n == 0):
        return 2;
    return 2 * prog(n-1) - 3;
print(prog(3))

#EX 2
def fibonacci( n ):
    if( n == 1 ):
        return 1;
    elif n == 0:
        return 0;
    else:
        return fibonacci(n-1) + fibonacci(n-2);
print(fibonacci(6));

#EX 3
def sumaN(n):
    if ( n == 1 ):
        return 1;
    else:
        return n + sumaN(n-1);
print(sumaN(5));

#EX 4
#a
def produs( n ):
    if ( n < 10 ):
        return n;
    else:
        return n%10 * produs(n // 10);
#b
def nrcif(n):
    if ( n < 10 ):
        return 1;
    else:
        return 1 + nrcif ( n // 10 ); 
#c
def maxim(n):
    if ( n < 10 ):
        return 1;
    else:
        return max( n % 10, maxim( n // 10 ) );
#d
def nrcp( n ):
    if( n < 10 ):
        return 1;
    else:
        return (( n % 10 ) % 2 == 0 ) + nrcp(n // 10);
print( produs ( 123 ), nrcif (276), maxim(4395), nrcp ( 24593 ) );

#EX 5
def putere( a, n ):
    if ( n == 0 ):
        return 1;
    else:
        return a * putere ( a, n-1 );
print ( putere(2,3));

#EX 6
def prim( n, div=2 ):
    if ( n < 2 ):
        return False;
    if ( n == 2 ):
        return True;
    if( n % div == 0):
        return False;
    if(div * div > n):
        return True;
    return prim(n, div + 1);

print(prim(17));

#EX 7
def cmmdc ( a, b ):
    if ( b == 0 ):
        return a;
    else:
        return cmmdc( b, a%b );
print ( cmmdc ( 48, 18 ));

#EX 8

def my_reverse ( sir ):
    if (len(sir)<=1):
        return sir;
    else:
        return my_reverse( sir[1:]) + sir [0];
print(my_reverse("Hello"));

#EX 9

def interval(min_value, max_value):
    if ( min_value < max_value ):
        print ( min_value + 1 );
        interval(min_value + 1, max_value);

print(interval(1,10));


#10
#a
def aparitii( n, k ):
    if ( n==0 ):
        return False;
    elif ( n % 10 == k ):
        return True;
    else:
        return aparitii( n // 10, k);

n=1254;
p= 3;
if( aparitii(n,p)):
    print("da");
else:
    print("nu"); 

#b
def ap (n, k) :
    if ( n==0 ):
        return 0;
    if ( n % 10 == k ):
        return 1 + aparitii( n // 10, k);
    return aparitii( n // 10, k);

n=133;
p=3;
c=ap(n,p)
print (c);

#11

def palindrom(n):
    def aux(t, inv):
        if ( n==inv ):
            return n == inv;
        else:
            inv = inv * 10 + t % 10;
            return aux( t // 10, inv );
    if( n < 0 ):
        return False
    else:
        return aux(n,0);
print ( palindrom ( 121 ) );

#12

def compf( f, x, n ):
    if ( n == 1 ):
        return  f( x );
    else:
        return f ( compf ( f, x, n-1) );
def fun(y):
    return y * 2 + 3;

print ( compf (fun, 4, 3) )

#14
def binar ( n ):
    if ( n == 0 ):
        return '';
    else:
        return binar(n // 2) + str(n%2);

print (binar(5));
        
#15

def triunghi( n ):
    if ( n >  0):
        triunghi(n-1);
        print ((str(n) + ' ') * n);

triunghi ( 5 );

#16

def putmin( a, p):
    def aux( k, ak,ex ):
        if ( ak == 1 ):
            return ex;
        else:
            return aux( k, (ak * a) % p, ex + 1);

    if ( a%p==0 ):
        return 0;
    else:
        return aux(a, a, 1);

print ( putmin(4,7));
    
    
'''
REZULTATE AFISARE

-5
8
15
6 3 9 2
8
True
6
olleH
2
3
4
5
6
7
8
9
10
None
nu
2
True
53
101
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
3
'''
        
        
        
        
    
