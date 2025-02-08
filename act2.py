def cost_of_hotel(nights):
    return nights*200
def flight_fee(city):
    if city=="Andijan":
        return 600
    elif city=="Tashkent":
        return 650
    elif city=="Namangan":
        return 700
    else:
        return 1000
def car_rental(days):
    if days>=7:
        return days*300-50
    elif days>=3:
        return days*300-20
    else:
        return days*300
def total_cost(nights,city,days,extramoney):
    return cost_of_hotel(nights)+flight_fee(city)+car_rental(days)+extramoney
print("Price of hotel",cost_of_hotel(7))
print("Price of flight",flight_fee("Andijan"))
print("Price of car rental",car_rental(10))
print("Total price",total_cost(7,"Andijan",10,1000))
