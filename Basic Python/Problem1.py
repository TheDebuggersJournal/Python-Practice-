def arithmatic_operations(integer1,integer2):
    print(''' List of Available operations:
          1. Addition
          2. Subtraction
          3. Multiplication
          4. Division
          5. Floor Division
          6. Modulus
          7. Exponential
          8. Exit
''')
    while True:
        choice = int(input("Enter your choice: "))
        try:

            if choice == 1:
                result = integer1+integer2
                print(result)
            elif choice == 2:
                result = integer1-integer2
                print(result)
            elif choice == 3:
                result = integer1 * integer2
                print(result)
            elif choice == 4:
                result = integer1/integer2
                print(result)
            elif choice == 5:
                result = integer1//integer2
                print(result)
            elif choice == 6:
                result = integer1 % integer2
                print(result)
            elif choice == 7:
                result = integer1 ** integer2
                print(result)
            elif choice == 8:
                print("Thankyou for using!!!")
                break
            else:
                print("Invalid Input")
            
        except ZeroDivisionError:
            print("Number cannot be divisible by zero")        



integer1 = int(input("Enter first integer: "))
integer2  = int(input("Enter second integer: "))
print(arithmatic_operations(integer1,integer2))
