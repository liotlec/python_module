def input_temperature(temp_str):
    print("Input data:", temp_str)
    temp = int(temp_str)
    if temp > 40:
        raise ValueError(temp_str + "°C is too hot for plants (max 40°C)")
    if temp < 0:
        raise ValueError(temp_str + "°C is too cold for plants (min 0°C)")
    return temp

def test_temperature():
    for value in ["25","abc","100","-50"]:
        try:
            temp = input_temperature(value)
            print("Temperature is now", temp)
        except ValueError as error:
            print(f"Caught input_temperature error:",error)
    print()
    print("All tests completed - program didn't crash!")        

print("=== Garden Temperature ===")
print()
test_temperature()
    