
# st="heolo world"
# # print(st.upper())

# # for i in range(len(st)):
# #     if st[i]==0 or st[i]==len(st)-1:
# #         st[i]=st[i].upper()
# #     print(st[i],end=' ')

# res=st[0].upper()+st[1:6]+st[6].upper()+st[7:]  
# print(res)


# print()

#  ----------------------------------------------------------------------------------  

# l=[1,2,3]

# c=0
# for i  in l:
# 	c+=1
# n=c-1
# q=0
# while n>=q:
# 	l[q],l[n]=l[n],l[q]
# 	q+=1
# 	n-=1
# print(l) 

#  ----------------------------------------------------------------------------------  

# def bsearch(n,k):
#     n.sort()
#     low=0
#     high=len(n)-1
#     while low<=high:
#         mid=(low+high)//2
        
#         if n[mid]==k:
#             return mid
#         elif n[mid]<k:
#             low=mid+1
#         else:
#             high=mid-1
#     return -1
# k=bsearch([31,2,3,4,63,63,7],63)          
# print(f"Element found at pos {k+1}")  


#  ----------------------------------------------------------------------------------           

# find nodes in list with given value then delete the previous node of that matched        

# class Node:
#     def __init__(self,data=None,next=None):
#         self.data=data
#         self.next=next
        

# def del_node(self,head,data):
#     dummy=Node(next=head)
#     left=dummy
#     right=head.next
    
#     while right:
#         if right.data==data:
#             left.next=left.next.next
#             break
#         left=left.nexxt
#         right=right.next    
        
#     return dummy.next    


# -----------------------------------------------------    


# def replacechar(str,old,new):
#     res=''
    
#     for i in str:
#         if i==old:
#             res+=new
#         else:
#             res+=i        
#     return res 

# print(replacechar("hwllo",'h','H'))

# -----------------------------------------------------------------

# def replacestr(n):
#     w=n.split()
#     r=[]
#     for i in w:
#         r.append(i[0].upper()+i[1:])
       
#     res=" ".join(r)
    
#     print(res)    
            
# replacestr("hello world")

# -----------------------------------------------------------------------

#reversing str using list

# str="hello world"
# str=list(str)
# i,h=0,len(str)-1
# while i<=h:
#     str[i],str[h]=str[h],str[i]
#     i+=1
#     h-=1
# str=''.join(str)    
# print(str)  

# -----------------------------------------------------------------------

# def cap(str):
#     f=1
#     c=[]
    
#     for i in str:
#         if f==1:
#             c.append(i.upper())
#             f=0
#         else:
#             c.append(i)
            
            
#         if i.isspace():
#             f=1
            
#     r="".join(c)               
#     print(r)
    
# cap("hello world")    
    
    

# -----------------------------------------------------------------------

# str=[" hello world"]
# c=[]
# for i in str:
#     for j in  i.split():
#         c.append(j[0].upper()+j[1:])
# r=' '.join(c)
                
# print(r)
    
    
    
    