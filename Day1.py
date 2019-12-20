import math

def FuelRequiredToLaunch(mass):
    return (math.floor(mass / 3)) - 2

def FuelSum(filename):
    with open(filename) as f:
        lines = f.readlines()
    
    total = 0
    for line in lines:
        fuel = FuelRequiredToLaunch(int(line))
        while(fuel > 0):
            total = total + fuel
            fuel = (math.floor(fuel / 3)) - 2


    return total

print(FuelSum("data.txt"))