# class node represents an individual elements in a linked list
# data can contain integers numbers or complex objects
#next is a pointer to the next element

class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next= next
        
        
class Linked_list:
    def __init__(self):
        self.head=None
        
    def insert_at_begining(self,data):
        new_node=Node(data,self.head)
        self.head=new_node
        
    def disp(self):
        if self.head is None:
            print("LInked list is empty")
            
        current=self.head
        while current:
            print(current.data,end=" -> ")
            current=current.next   
        print("None")
        
    # def disp(self):
    #     if self.head is None:
    #         print("Linked lilst is empty")
    #     current=self.head
    #     l=''
        
    #     while current:
    #         l+=str(current.data)+' -> '
    #         current=current.next 
            
    #     print(l) 
    #     print(type(l))     

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        
        current=self.head
        while current.next:
            current=current.next
            
        current.next=Node(data,None)    
                
    def insert_values_end(self,data_list):
        # self.head=None     
        for data in data_list:
            self.insert_at_end(data)       
            
    def insert_values_beg(self,data_list):    
        for data in data_list[::-1]:
            self.insert_at_begining(data)       
            

    def get_length(self):
        c=0
        itr=self.head
        while itr:
            c+=1
            itr=itr.next
            
        return c
    
    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("Not a valid Index")     
                
        if index==0:
            self.head=self.head.next
            return        
        
        c=0
        itr=self.head
        while itr:
            if c==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            c+=1
           
    def insert_at(self,index,data):
        if index<0 or index>=self.get_length():
            raise Exception("Not a valid Index")
        
        if index==0:
            self.insert_at_begining(data)
            return
        
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1
            
             
    def remove_duplicates(self):
        current = self.head
        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next      
 
ll=Linked_list()

ll.insert_at_begining(4)    
ll.insert_at_begining(1)
ll.insert_at_begining(4)
ll.insert_values_end(["11","22","33"])


ll.insert_at_end(67)

ll.insert_values_beg(["mm","aa",'ss'])
ll.insert_at(0,"qq")


print(ll.get_length())
# ll.remove_at(5)

ll.disp()






            


        