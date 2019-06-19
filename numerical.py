#funstion to check prime

def isPrime(n):
   f=True
   for i in range (2,n):
       if n%i==0:
           return False
   return f

def factorial(n):
   s=1
   for i in range(1,n+1):
       s=s*i
   return s

def upper(S):
   return S.swapcase()

