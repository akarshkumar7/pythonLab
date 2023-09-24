class Data:
    pass
class Number(Data):
    def is_palin(self, data):
        rev = 0
        temp = data

        while temp > 0:
            digit = temp % 10
            rev = rev * 10 + digit
            temp = temp // 10

        if data == rev:
            print("palindrome")
        else:
            print("not palindrome")

class String(Data):

    def is_palin(self, data):
        if data == data[::-1]:
            print("palindrome")
        else:
            print("not palindrome")

x = input("enter the string :")
str = String()
str.is_palin(x)

y = int(input("enter the number :"))
num = Number()
num.is_palin(y)


