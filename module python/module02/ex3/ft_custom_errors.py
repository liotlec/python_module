class GardenError(Exception):
    pass

class PlantError(Exception):
    pass

class WaterError(Exception):
    pass

def checkWater(water):
    if water < 10:
        raise WaterError(f"Not enough water in the tank!")

def checkPlant(plant):
    if plant == "tomato":
        raise PlantError(f"The {plant} plant is wilting!")

def checkGarden(water, plant):
    try:
        checkWater(water)
        checkPlant(plant)
    except (WaterError, PlantError) as error:
        raise GardenError(f"{error}")

print("=== Garden Custom Errors Demo ===")
print("Testing PlantError...")
try:
    checkPlant("tomato")
except PlantError as error:
    print(f"Caught PlantError: {error}")
print("Testing WaterError...")
try:
    checkWater(5)
except WaterError as error:
    print(f"Caught WaterError: {error}")
print("Testing GardenError...")
try:
    checkGarden(5, "tomato")
except GardenError as error:
    print(f"Caught GardenError: {error}")
try:
    checkGarden(15, "tomato")
except GardenError as error:
    print(f"Caught GardenError: {error}")
print("All custom error types work correctly!")