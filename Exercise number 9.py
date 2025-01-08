price = float(input("Enter the price of your purchase to find out your discount: "))

def discount():
    price_discount = 0
    if price < 100:
        final_price = price - price * price_discount/100
        print(f"Your discount is 0%. The price of your purchase is {final_price}.")
    elif price >= 100 and price < 200:
        price_discount = 10
        final_price = price - price * price_discount/100
        print(f"Your discount is {price_discount}%. The price of your purchase is {final_price}.")
    elif price >= 200 and price < 500:
        price_discount = 15
        final_price = price - price * price_discount/100
        print(f"Your discount is {price_discount}%. The price of your purchase is {final_price}.")
    else:
        price_discount = 25
        final_price = price - price * price_discount/100
        print(f"Your discount is {price_discount}%. The price of your purchase is {final_price}.")

discount()