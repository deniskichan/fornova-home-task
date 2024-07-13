import json

cheapest_price = float("inf");
cheapest_room_type = ""
cheapest_guests = 0
total_prices = {}

with open('Python-task.json', 'r') as file:
    data = json.load(file)

for assignment_result in data["assignment_results"]:
    prices = assignment_result["shown_price"]
    currency = assignment_result["currency"]
    
    for room_type, price in prices.items():
        price_float = float(price)
        if price_float < cheapest_price:
            cheapest_price = price_float
            cheapest_room_type = room_type
            cheapest_guests = assignment_result["number_of_guests"]
        
        taxes = assignment_result["ext_data"]["taxes"].replace("{", "").replace("}", "").replace("\"", "").replace(":", " ").replace(",", " ").split()
        tax_amount = float(taxes[1]) + float(taxes[4])
        total_price = price_float + tax_amount
        
        total_prices[room_type] = round(total_price, 2)

with open("output.txt", "w") as file:
    file.write(f"The cheapest room type is {cheapest_room_type} with a price of {cheapest_price} {currency} for {cheapest_guests} guests.\n")
    file.write("Total prices for all rooms:\n")
    for room_type, price in total_prices.items():
        file.write(f"{room_type}: {price} {currency}\n")

