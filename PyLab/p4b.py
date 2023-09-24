def romantoint(roman):
    roman_num={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total=0
    prev_val=0
    for i in reversed(roman):
        value=roman_num[i]

        if value <prev_val:
            total-=value
        else:
            total+=value
        prev_val=value
    return total

roman=input('enter the roman numerals :').upper()
result=romantoint(roman)
print(f'the integer value :',result)