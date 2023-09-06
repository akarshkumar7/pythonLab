class Data:
    pass
class Number(Data):
    def is_palin(self, data):
        rev = 0
        temp = data

        while temp > 0:
            dig = temp % 10
            rev = rev * 10 + dig
            temp = temp // 10

        if data == rev:
            print("Palindrome")
        else:
            print("Not palindrome")


class String(Data):
    def is_palin(self, data):
        if data == data[::-1]:
            print("Palindrome")
        else:
            print("Not palindrome")


string = input("Enter string: ")
str = String()
str.is_palin(string)


number = int(input("Enter number: "))
num = Number()
num.is_palin(number)