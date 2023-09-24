import difflib

str1=input("enter the string1")
str2=input('enter r the string2')

def string_simil(str1,str2):
    result=difflib.SequenceMatcher(a=str1.lower(),b=str2.lower())
    return result.ratio()

print(str1)
print(str2)
print(f"similarity",string_simil(str1,str2))