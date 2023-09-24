def btod(bin):
    dec,p=0,0
    while(bin!=0):
        rem=bin%10
        dec=dec+rem*2**p
        bin=bin//10
        p+=1
    return dec

def octtohex(n):
    n=int(n,8)
    print("decimal equivalent to octal=",n)
    hexa=hex(n)
    return (hexa)

n=int(input('enter the binary '))
print("equivalent decimal is ",btod(n))

n=input("enter the ocatal numbers (0-7)")
# n='0o'+n
# print("octal represention of ",n)
print("equivalent hexadecimal value is:",octtohex(n))
