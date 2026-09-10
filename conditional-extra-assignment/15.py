cost_price=int(input("Enter cost price:-"))
selling_price=int(input("Enter selling price:-")) 


if selling_price>cost_price:
    profit = selling_price-cost_price
    profit_percentage =(profit/cost_price*100)
    print("Profit:-", profit)
    print("profit percentage:-", profit_percentage)
elif cost_price>selling_price:
    loss = cost_price-selling_price
    loss_percentage =(loss/cost_price*100)
    print("Loss:-", loss)
    print("Loss percentage:-", loss_percentage)

