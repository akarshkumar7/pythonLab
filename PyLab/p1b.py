n=(input('enter the number'))
rev=n[::-1]

if n==rev:
    print('pallindrome')
else:
    print('not')

freq={}

for i in n:
    freq[i]=n.count(i)
print(freq)
