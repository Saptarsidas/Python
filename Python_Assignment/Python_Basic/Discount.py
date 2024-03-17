#Create a Python program that calculates the discount amount based on the purchase amount using if-else.
purchase=int(input("Enter bill amount: "))
if purchase>=5000:
    discount=purchase*0.1
    #10% discount
elif purchase>=1000:
    discount=purchase*0.5
    #5% discount
else:
    discount=0
Final=purchase-discount
print("Purchase Amount:", purchase)
print("Discount Amount: ", discount)
print("Final Amount after Discount: ", Final)