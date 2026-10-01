amount=float(input("enter p[urchase amount:"))

if amount <1000:
       discount = amount *5 / 100
 elif amount < 5000:
       discount = amount *10 / 100
else:
       discount = amount *15 / 100



net_payable = amount - discount

print("purchase amount :", amount)
print("discount:", discount)
print("net payable:",net_payable)
