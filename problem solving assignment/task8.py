count=0
budget_product=0
luxury_product=0
regular_product=0
premium_product=0

for i in range(1,9):
    price=int(input(f"Enter price of product {i}:-")) 
    if price>=5000:
        count=count+price
        luxury_product+=1
        print("Luxury")
    elif price>=2000:
         count=count+price
         premium_product+=1
         print("Premium")
    elif price>=500:
         count=count+price
         regular_product+=1
         print("Regular")
    elif price<500:
         count=count+price
         budget_product+=1
         print("Budget") 

total= count 
print("Total Amount:-",total)  
Average_Price=total/5
print("Average price of products:-",Average_Price)  
 
print("Luxury products:-", luxury_product)
print("Premium products:-", premium_product)
print("Regular products", regular_product)
print("Budget products:-", budget_product) 
