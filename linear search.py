# runtime complexity=O(n)

# they dont need to be sorted
# useful for small datasets
# useful for ds that do not random access(Linked List)



# def lsearch(n,k):
#     f=0
#     for i in range(len(n)):
#         if n[i]==k:
#             f=1
#             print(f"The element {k} found at index {i} ")
#     if f==0:
#         print(f"The element {k} is not found")    
        
# lsearch(arr,18)

# -----------------------------------------------------------


arr=[9,2,8,3,7,3,6,4,5]
def lser(n,k):
    for i in range(len(n)):
        if n[i]==k:
            return i
    return 1

# k=61
k=7
res=lser(arr,k)

if res!=1:
    print(f"the element {k} found at {res} ")
else:
    print(f"The element {k} is not found")  
        
        
        
            
            
        