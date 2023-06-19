# This module will add items(products) from a shopping cart and calculate the subtotal, grand total after filtering the items whether taxable or not and considering discount from a json file.

import json

shopping_cart = [{'name': 'Apple', 'price': 0.25, 'isTaxable': False},                             
             {'name': 'Bread', 'price': 0.5, 'isTaxable': True},
             {'name': 'Egg',   'price': 0.35, 'isTaxable': True},
             {'name': 'Butter', 'price': 0.50, 'isTaxable': True}
]

coupon_file = 'coupon.json'

tax_rate = 0.0725

def calculate_shopping_cart(tax_rate, coupon_file, shopping_cart):
    with open(coupon_file) as file:
         coupon = json.load(file)
    sub_total = 0
    total_tax = 0    
    # Iterate through cart to calulate sub total
    for item in shopping_cart:
        sub_total += item['price']
        if item['name'] in coupon:
           discount = coupon[item['name']]
           sub_total -= min(discount, item['price'])
        if item['isTaxable']:
           total_tax = item['price'] * tax_rate
        grand_total = max(0, sub_total + total_tax)
    s_total = '%.3f'%sub_total
    d_count = '%.3f'%discount
    t_payable = '%.3f'%total_tax
    g_total = '%.3f'%grand_total
    return s_total, d_count, t_payable, g_total, shopping_cart 
s_total, d_count, t_payable, g_total, v_cart = calculate_shopping_cart(tax_rate, coupon_file, shopping_cart)

print("Subtotal: $",s_total+"\n"+"discount applied: $",d_count+"\n"+"total tax charged: $", t_payable+"\n"+"grand total: $", g_total)

for item in v_cart:
    print(item)

                                             


