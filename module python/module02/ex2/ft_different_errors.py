def garden_operations(operation_number):
    try:
        if operation_number == 0:
            int("abc")
        elif operation_number == 1:
            10 / 0  
        elif operation_number == 2:
            open("/non/existent/file")
        elif operation_number == 3:
            "abc" + 5
        elif operation_number == 4:
            int(4)
    except (ValueError, TypeError, ZeroDivisionError, FileNotFoundError) as error:
        print(f"Caught {type(error).__name__}: {error}")
    else:
        print("Operation completed successfully.")

print("=== Garden Error Types Demo ===")
for i in range(5):
    print("Testing operation " + str(i) + "...")
    garden_operations(i)
print()
print("All error types tested successfully!")
