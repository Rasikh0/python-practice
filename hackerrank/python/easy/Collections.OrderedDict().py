from collections import OrderedDict

n = int(input())
item_dict_ordered = OrderedDict()
for i in range(n):
    # 1. receive the item
    item, price = input().strip().rsplit(' ', 1) # rsplit(' ', 1) breaks into ['Banana fries', 2] instead of ['Banana', 'fries', 2]. That 1 indicates how many times to split from right. 
    price = int(price)
    
    # 2. check if the item exists in the dict, if not add it
    if item in item_dict_ordered:
        item_dict_ordered[item] += price
    else:
        item_dict_ordered[item] = price
        
for item, price in item_dict_ordered.items():
    print(item, price)
