
cost_price=int(input("Enter a cost_price"))
selling_price=int(input("Enter a selling_price"))
if selling_price>cost_price:
    print("profit")
elif selling_price<cost_price:
    print("loss")
elif selling_price==cost_price:
    print("No profit and No loss")