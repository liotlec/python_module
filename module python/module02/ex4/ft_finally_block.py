class PlantError(Exception):
    pass

def water_plant(plant_name):
    if plant_name[0] == str.capitalize(plant_name[0]):
        print(f"Watering the {plant_name} plant...")
    else:
        raise PlantError(f" Invalid plant name to water: {plant_name}")

def test_watering_system(table_of_plants):
    for plant in table_of_plants:
        try:
            water_plant(plant)
        except PlantError as error:
            print(f"Caught PlantError: {error}")
            print("Ending tests and returning to main...")
            return(print("Closing watering system"))
    print("Closing watering system")

print("=== Garden Watering System ===")
print("Testing valid plants...")
test_watering_system(["Rose", "Tulip", "Daisy"])
print("Testing invalid plants...")
test_watering_system(["lettuce", "tulip", "daisy"])

print("Cleanup always happens, even with errors!")
