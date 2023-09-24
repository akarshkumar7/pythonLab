def insertion(lst):
    for i in range(1,len(lst)):
        key = lst[i]
        j = i - 1
        while j>=0 and key<lst[j]:
            lst[j+1] = lst[j]
            j = j - 1
        lst[j+1] = key

def merge(lst):
    if len(lst)>1:
        mid = len(lst)//2
        lhalf = lst[:mid]
        rhalf = lst[mid:]
        merge(lhalf)
        merge(rhalf)
        i=j=k=0
        while i<len(lhalf) and j<len(rhalf):
            if lhalf[i]<rhalf[j]:
                lst[k] = lhalf[i]
                i += 1
            else:
                lst[k] = rhalf[j]
                j += 1
            k += 1
        while i<len(lhalf):
            lst[k] = lhalf[i]
            i += 1
            k += 1
        while i<len(lhalf):
            lst[k] = rhalf[j]
            j += 1
            k += 1
        return lst

lst = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    a = int(input())
    lst.append(a)
print("1.Insertion_sort\n2.Merge_sort")
c = int(input("Enter the choice: "))
match(c):
    case 1:
        insertion(lst)
        print(lst)
    case 2:
        merge(lst)
        print(lst)
    case _:
        print("Enter a valid list")