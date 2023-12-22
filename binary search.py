#sorted array
#half of the array will be eliminated at each step   

a=[1,2,3,4,5,6,7,8]

def bsearch(n,k):
    low=0
    high=len(a)-1
    while low<=high:
        mid=(low+high)//2
        
        if n[mid]==k:
            return mid
        elif n[mid]<k:
            low=mid+1
        else:
            high=mid-1
    return -1

k=8
print(f"element {k} found at index: {(bsearch(a,4))}")        
                
            
             
   
        