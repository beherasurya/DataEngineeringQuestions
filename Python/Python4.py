
list1 = [1,2,5,1,9,10,23,2,1,1]
#Write a python function to find the duplicate numbers

def find_duplicate(numberlist):
    dup = []
    set1 = set()
    for num in numberlist:
        if num in set1:
            dup.append(num)
        else:
            set1.add(num)
    return list(set(dup))

print(find_duplicate(list1))