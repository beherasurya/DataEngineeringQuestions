
prices = [10,20,25,None]
#output - whenever you find none add the avg value of the price list

def calc_price(pricelist):
    total_price = 0
    for i in pricelist:
        if(type(i) is int):
            total_price+=i
    for i in range(len(pricelist)):
        if(type(pricelist[i]) is not int):
            pricelist.remove(pricelist[i])
            pricelist.append(total_price/len(pricelist))
    return pricelist
print(calc_price(prices))