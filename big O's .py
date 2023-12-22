#-------------------------------------------#
# O(1)  - Constant Time

num=[1,2,3]
num.append(4) # push to end
num.pop() # remove from end
num[0]  #lookup
num[1]

# Hash Map/ Set
hashMap = {}
hashMap["key"] = 10 # insert
print("key" in hashMap) #lookup
print(hashMap["key"])
hashMap.pop("key")   

#-------------------------------------------#
# O(log n) - Logarithmetic Time

#binary search
def binserach(num,k):
    l,h=0,len(num)-1

    while l<=h:
        mid=(l+h)//2
        if k==mid:
            return num[mid]
        elif k<mid:
            h=mid-1
        else:
            l=mid+1 
                       
#-------------------------------------------#
# O(n) - Linear Time

num=[1,2,3]
sum(num)  #sum of array
for i in num:   #looping through
    print(i)
    
num.insert(1,100)    # inserting in the middle
num.remove(100)     # removing from the middle

#-------------------------------------------#
# O(n^2) - Quadratic Time
#   traverse  a square grid

num=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(num)):
    for j in range(len(num[i])):
        print(num[i][j],end=' ')
        
# Get every pair of elements in an array
num=[1,2,3]
for i in range(len(num)):
    for j in range(i+1,len(num)):
        print(num[i],num[j])

#insertion sort



# num=[1,2,3,4,5,6]   # O(n*m)
# for i in range(len(num)):
#     for j in range(i+1,len(num)):
#         for m in range(j+1,len(num)):
#             print(num[i],num[j],num[m])
        
    
        
# ---------------------------------------------------------

# O(n logn)

# merge sort()

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    
    left=merge_sort(left)
    right=merge_sort(right)
    
    return merge(left,right)

def merge(left,right):
    res=[]
    l,r=0,0
    
    while l<len(left) and r<len(right):
       if left[l]<right[r]: 
            res.append(left[l])
            l+=1
       else:
           res.append(right[r]) 
           r+=1
           
    res.extend(left[l]) 
    res.extend(right[r])      
    
    return res  