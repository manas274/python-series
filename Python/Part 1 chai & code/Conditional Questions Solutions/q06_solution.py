# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

Distance = int(input("How much distance: "))

if Distance < 3:
    print("Walk")
    
elif 3 <= Distance <= 15:
    print("Bike")
    
else:
    print("Car")
