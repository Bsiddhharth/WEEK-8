def fiba(n):
    a,b=0,1
    c=0
    
    while c<n:
         print(a,end=" ")
         a,b=b,b+a
         c+=1
         

fiba(11)   
print()      

def fibonacci(n):
  
    if n == 0 or n == 1:
        return n
    
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


result = fibonacci(6)
print("Fibonacci sequence at position 6 is:", result)

