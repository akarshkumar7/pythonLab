import re
def isphonenumber(no):
    if len(no) != 12:
        return False

    for i in range(len(no)):
        if no[i] == '-':
            continue
        elif no[i].isdigit():
            continue
        return False
    return True

def checkphone(no):
    pp = re.compile(r'^\d{3}-\d{3}-\d{4}$')
    if pp.match(no):
        return True
    return False

no = input("Enter the phone number: ")
print(isphonenumber(no))
print(checkphone(no))
# print('without regular expression')
# if isphonenumber(no):
#     print("valid")
# else:
#     print('invalid')
