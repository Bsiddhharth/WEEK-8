# #factorial
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
    
# n=int(input("Enter the number to find the factorial: "))

# print(fact(n))

# #printing reverse  of 100 numbers using recursion

# def rev(n):
#     while n>0:
#         return rev(n-1)

# print(rev(100))

#bsearch using recursion
# def bsearch(n,low,high,target):
#     n.sort()
#     if low>high:
#         return -1
    
#     mid=(low+high)//2
    
#     if n[mid]==target:
#         return mid
#     elif n[mid]<target:
#         return bsearch(n,mid+1,high,target)
#     else:
#         return bsearch(n,low,mid-1,target)
    
    
# n=[11,2,3,44,5,6,7,8]    

# k=bsearch(n,0,len(n)-1,5)
# print(f"The element is found at pos {k+1}")  


# def rev(s):
#     if len(s) == 0:
#         return s
#     else:
#         return rev(s[1:])+s[0]
    
# stri="string"    
# print(rev(stri)  )


# def bsrev(a,low,high,target):
#     if low>high:
#         return -1
#     mid=(low+high)//2
#     if a[mid]==target:
#         return mid
#     elif a[mid]<target:
#         return bsrev(a,mid+1,high,target)
#     else:
#         return bsrev(a,low,mid-1,target)
    
# --------------------------------------------

# def rev_list(self,head):
#     if not head:
#         return None
    
#     new=head
#     if head.next:
#         new=self.rev_list(head.next)
#         head.next.next=head
#     head.next=None    

# -------------------------------------------------

