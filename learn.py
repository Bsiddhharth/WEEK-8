# class Node:
#     def __init__(self,data=None,next=None):
#         self.data=data
#         self.next=next
        
# class Linked_list:
#     def __init__(self):
#         self.head=None
        
#     def insert_at_beg(self,data):
#            newnode=Node(data,self.head)
#            self.head=newnode
           
#     def insert_at_end(self,data):
#         if self.head is None:
#             self.head=Node(data,None) 
#             return
         
#         itr=self.head
#         while itr.next:
#             itr=itr.next
#         itr.next=Node(data)    
            
                      
           
#     def disp(self):
#         if self.head is None:
#             raise Exception("nothing to print")
        
#         itr=self.head
#         while itr:
#             print(itr.data,end=' -> ')       
#             itr=itr.next
            
#         print("None")    
        
#     def get_length(self):
#         c=0
#         itr=self.head
#         while itr:
#             c+=1
#             itr=itr.next 
#         return c
           
#     def remove_at(self,index):
#         if index<0 or index>=self.get_length():
#             raise Exception("invalid nothing to remove")
#         if index==0:
#             self.head=self.head.next
#             return
#         c=0
#         itr=self.head
#         while itr:
#             if c==index-1:
#                 itr.next=itr.next.next
#                 return 
#             c+=1
#             itr=itr.next       
    
#     def insert_at(self,index,data):
#         if index<0 or index>self.get_length():
#             raise Exception("invalid position for inserting data")
#         if index==0:
#             self.insert_at_beg(data)
#         c=0
#         itr=self.head
#         while itr:
#             if c==index-1:
#                 newnode=Node(data,itr.next)
#                 itr.next=newnode
#                 break
#             c+=1
#             itr=itr.next
    
#     def insert_after_val(self,data_after,data):
#         if self.head  is None:
#             return
        
#         if self.head.data==  data_after:
#             self.head.next=Node(data,self.head.next)
            
#         itr=self.head
#         while itr:
#             if itr.data==data_after:
#                 itr.next=Node(data,itr.next)
#                 break
#             itr=itr.next
            
                
                    
                
     
# l=Linked_list()
# l.insert_at_beg(2)        
# l.insert_at_beg(22)          

# l.insert_at_end(67)      
# l.insert_at_end(21)     

# # l.remove_at(0)  
# l.insert_at(2,90)
# l.insert_at(0,80)
              
# l.disp()              


# a=[4,32,1,3]
# a.sort()
# print(2*a)



                          