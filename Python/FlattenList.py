#Python Question asked in Deloitte

# list1 = [10,20,[90,80],[20,30,40],[14,20]]
# output = [10,20,90,80,20,30,40,14,20]
list1 = [10,20,[90,80],[20,30,40],[14,20]]
def conv_nested_list(input_list):
    result_list = []
    for i in input_list:
        if(type(i) is list):
            result_list.extend(conv_nested_list(i))
        else:
            result_list.append(i)
    return result_list


print(conv_nested_list(list1))