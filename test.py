# a="123"

# print(a[::-1])
 
# i=0
# h=len(a)-1 
# a=list(a)

# while i<=h:
#     a[i],a[h]=a[h],a[i]
#     i+=1
#     h-=1
#     rev="".join(a)
    
    
# print(type(a))
# print(int(rev))
       
# str="hi hello whatsup"

# i,h=0,len(str)-1
# str=list(str)
# while i<=h:
#     str[i],str[h]=str[h],str[i]
#     i+=1
#     h-=1
#     res=''.join(str)
    
# print(type(str))    
# print(res)    


# def capi(str):
#     w=str.split()
    
#     res=[]
    
#     for i in w:
#         res.append(i[0].upper()+i[1:])
    
#     c=" ".join(res)
#     print(res)       
#     print(c)   
#     print(type(c))         
# capi("hello world")               


str="hello worlds"

def cap(str):
    w=str.split()
    
    r=[]
    
    for i in w:
        r.append(i[0].upper()+i[1:])
    
    res=' '.join(r)    

    print(res)
    
cap(str)    
    

        