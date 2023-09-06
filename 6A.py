filename=input("file name:")
f1=open(filename,"r")
n=int(input('enter the no. of lines to be displayed:'))

count=1
for line in f1:
    print(line,end="")
    if count==n:
        break
    count=count+1

f1.close()
f1=open(filename).read()

word=input('enter the word to be counted for frequency:')

print(f"freq of word'{word}':{f1.count(word)}")