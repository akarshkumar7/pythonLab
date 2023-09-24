frame =input('enter the file name')
file1=open(frame,"r")

n=int(input("how many lines"))
count=1
for line in file1:
    print(line,end=' ')
    if count==n:
        break
    count+=1
x=open(frame).read()
wordlist=x.split()
k=0
word=input("enter the word")
for w in wordlist:
    if w==word:
        k+=1

print('total freq of the word:',k)
