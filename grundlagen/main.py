def calculate_price(baseprice, specialprice, extraprice, extras, discount):
    if extras >= 5:
        addon_discount = 15
    elif extras >= 3:
        addon_discount = 10
    else:
        addon_discount = 0

    if discount > addon_discount:
        addon_discount = discount

    result = baseprice * (1 - discount/100) + specialprice + extraprice * (1 - addon_discount/100)
    return result
