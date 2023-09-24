
def fib(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fib(num-1)+fib(num-2)

n=int(input('enter a numbers'))

if n>0:
    print('the fibonacci series :')
    for i in range(0,n):
        print(fib(i),end=" ")


else:
    print('invlaid')


