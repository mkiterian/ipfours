def is_valid_IP(strng):
    strng_lst = strng.split()
    check = True
    
    if len(strng) < 1:
        check = False
    
    for item in strng_lst:
        if item.count('.') < 3:
            check = False
            break
        item_lst = item.split('.')
        
        for num in item_lst:
            if num[0] == '0':
                check = False
                break
            int_num = 0
            try:
                int_num = int(num)
            except ValueError:
                check = False
                
            if int_num > 255 or int_num < 0:
                check = False
                break
                
    return check
