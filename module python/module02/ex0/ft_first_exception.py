def input_temperature(temp_str):
    print("Input data:", temp_str)
    temp = int(temp_str)
    return temp

def test_temperature():
    for value in ["25","abc"]:
        try:
            temp = input_temperature(value)
            print("Temperature is now", temp)
        except ValueError as error:
            print(error)
    
    print()
    print("All tests completed - program didn't crash!")        

print("=== Garden Temperature ===")
print()
test_temperature()
