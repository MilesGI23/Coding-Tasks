# city_flight = input("Are you flying to Spain, Greece or France? ").lower()

# num_nights = int(input("How many nights are you staying for? "))

# def flight_cost(city, nights):
#     if city == "spain":
#         cost_per_night = 140
#     elif city == "greece":
#         cost_per_night = 150
#     elif city == "france":
#         cost_per_night = 90
#     else:
#         print("Invalid destination.")
#         return 0
    
#     return cost_per_night * nights

# plane_cost = flight_cost(city_flight, num_nights)

# print("The cost of your flight will be:", "€", plane_cost)
city_flight = input("Are you flying to Spain, Greece or France..?\n").lower()

num_nights = int(input("How many nights are you staying for..?\n"))

rental_days = int(input("How many days will be hiring the vehicle for.?\n"))


def cost_h (x,y=90):
    x = num_nights 
    return (x * y)

hotel_cost = cost_h(num_nights) 

print("The price of your hotel will be :","€",hotel_cost)

def flight_cost (City,nights):
    if City == "Spain":
        City = 140
    elif City == "greece":
        City = 150
    elif City == "france":
        City = 90
    else:
        print("invaild Destination")
        
    
    return (City * nights)

plane_cost = flight_cost(city_flight, num_nights)

print("The cost of your flight will be:","€",plane_cost)
        
    

def car_rent (x,y=65):
    x = int(rental_days)
    return(x*y)
    
car_rental = car_rent(rental_days)

print(f"The Price of the car rental will be :", "€", car_rental, "for", rental_days, "days")


def Holi_cost (car_rent,city_flight,num_night):
    return (car_rent + city_flight + num_night)

total_cost = Holi_cost(car_rental, plane_cost, hotel_cost)

print (f"The total price of your holiday will be: €{total_cost} for {num_nights} days.")
    
