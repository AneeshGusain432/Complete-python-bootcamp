order_size = "Medium"
extra_shot = True

if extra_shot:
    coffe = order_size + " coffee with an extra shot"
else:
    coffe = order_size + " coffee"
    
print("order:", coffe)