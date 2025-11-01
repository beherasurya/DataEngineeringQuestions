list1 = [10,3,2,0,23,199,0,22,0]

#output = [10,3,2,23,199,22,0,0,0]

def transform_list(input_list):
    for item in input_list:
        if(item == 0):
            input_list.remove(item)
            input_list.append(item)
    return input_list
print(transform_list(list1))