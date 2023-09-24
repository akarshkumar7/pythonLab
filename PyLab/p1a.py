a=int(input('mark1'))
b=int(input('mark2'))
c=int(input('mark3'))

total=int(a+b+c)

avg=(total-min(a,b,c))/2

print(f'the avg os best of two',avg)