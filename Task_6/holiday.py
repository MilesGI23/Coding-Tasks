city_flight = input("Are you flying to Spain, Greece or France..?\n").lower()

num_nights = int(input("How many nights are you staying for..?\n"))

rental_days = int(input("How many days will be hiring the vehicle for.?\n"))


def cost_h (nights,Cost_per_night=65):
    return (nights * Cost_per_night)

hotel_cost = cost_h(num_nights) 

print(f"The price of your hotel will be : €{hotel_cost}")

def flight_cost (City,nights):
    if City == "spain":
        City = 90
    elif City == "greece":
        City = 110
    elif City == "france":
        City = 65
    else:
        print("invaild Destination")
        
    
    return (City * nights)

plane_cost = flight_cost(city_flight, num_nights)

print(f"The cost of your flight will be: € {plane_cost}" )
        
    

def car_rent (number_of_days,cost_per_day=29):
    return(number_of_days * cost_per_day)
    
car_rental = car_rent(rental_days)

print(f"The Price of the car rental will be : €{car_rental} for {rental_days} days\n")


def Holi_cost (car_rent,city_flight,num_night):
    return (car_rent + city_flight + num_night)

total_cost = Holi_cost(car_rental, plane_cost, hotel_cost)

print (f"The total price of your holiday will be: €{total_cost} for {num_nights} days.\n")
    
