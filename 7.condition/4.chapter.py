
#another example
#300 se zayada amount par delivery fee 0 hai warna 30 charges delivery

order_amount = int(input("Enter the order amount:")) #first convert it to number
delivery_fee = 0 if order_amount > 300 else 30
# Ternary operator
# value_if_true if condition else else_value

# if order_amount > 300:
#     delivery_fee = 0
# else:
#     delivery_fee = 30

# print(f"Order amount: {type(order_amount)}")
print(f"Delivery fees is : {delivery_fee}")


