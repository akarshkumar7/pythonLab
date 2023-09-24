sen=input("enter the sentence")
u,l,d,w=0,0,0,0
w=len(sen.split())
for i in sen:
    if i.isupper():
        u+=1
    elif i.islower():
        l+=1
    elif i.isdigit():
        d+=1
print('words',w)
print('the uppercase',u)
print('digit',d)
print('lower',l)