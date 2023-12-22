# li=[1,3,4,6,7,8,11,3]

# def bsearch(n,k):
#     li.sort()
#     l,h=0,len(li)-1
    
#     while l<=h:
#         mid=(l+h)//2
        
#         if n[mid]==k:
#             return mid
#         elif n[mid]>k:
#             h=mid-1
#         else:
#             l=mid+1
            
# print(bsearch(li,11) )         

class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
        
class Linked_list:
    def __init__(self):
        self.head=None        
        
    def insert(self,data):
        node=Node(data,self.head)
        self.head=node 
    
    def disp(self):
        # if self.head is None:
        #    print("empty")
           
        itr=self.head

        while itr:
            print(itr.data,end=" ->")
            itr=itr.next
        print("None")
             
     
l=Linked_list()        
l.insert(5)
l.disp()
           