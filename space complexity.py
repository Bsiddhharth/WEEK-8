# O(1)
def c(n):
    res=1+1
    return res  #space compl is O(1) because the space used is same regardless of the input 

# O(log n)

def loggn(n):
    r=0
    while n>1:
        n//=2       #function uses a loop that repetedly divides input by 2 in each iteration until it reaches 1
        r+=1    # space compl is O(log n) because the space used grows logarithmically with the input
        
    return      

#O(n)

def inp(n):
    res=[0]*n
    for i in range(n):
        res[i]=i        #space used is directly proportional to input n
    return res    
    
inp(5)

#O(n log n)
def ss(n):
    a=[]
    for i in range(n):
        a.append(i)
    a.sort()                #Sorting takes O(n log n) spacec complexity
    return a    

# O(n^2)
def sqr(n):
    a=[]
    for i in range(n):
        b=[]
        for j in range(n):
            b.append(i+j)
        a.append(b)        
            
    # return res                    #the space used is proportional to the square of input
    print (a)     
    
sqr(2)    

#O(2^n)
def fiba(n):
    if n==1   or n==0:
        return n
    else:               #space coplexity is O(2^n) because each recursive call leads to two more recursive calls
        return fiba(n-1)+fiba(n-2)
  
c=fiba(6)   
print(c)


#O(n!):
def fact(n):
    if n==0 or n==1:
        return 1        #each recursive call multiplies the result by n times
    else:
        return n*fact(n-1)
    
     