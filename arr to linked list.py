class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
        
def arr_to_linked_list(arr) :
            if not arr:     # if array is empty
                return None
            
            
            head = Node(arr[0])
            current = head      # here both current and head are referencing same node
            
            for data in arr[1:]:
                current.next=Node(data)
                current = current.next
            
            while head:
                print(head.data,end=" -> ")
                head=head.next
            print("None")    
                
arr=[1,2,3,4]
arr_to_linked_list(arr)                
            

