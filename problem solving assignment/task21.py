bill_5000=0
bill_3000=0
bill_1000=0
bill=0
product_5000=0
product_3000=0
product_1000=0
product=0
for i in range(1,11):
    price=int(input("Enter price of {i} product")) 
    if price>=5000:
        bill_5000=price*0.2
        product_5000+=1
    elif price>=3000:
        bill_3000=price*0.15
        product_3000+=1
    elif price>=1000:
        bill_1000=price*0.1
        product_1000+=1
    elif price<1000:
        bill=price
        product+=1

total=(bill+bill_1000+bill_3000+bill_5000)    
print(total) 
print("Products receiving 20% discount", product_5000)
print("Products receiving 15% discount", product_3000)
print("Products receiving 10% discount", product_1000)
print("Products receiving no discount", product)
Discount_5000=product_5000*0.2
Discount_3000=product_3000*0.15
Discount_1000=product_1000*0.1 
total_Discount=(Discount_5000+Discount_3000+Discount_1000)*100


      