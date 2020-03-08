while True:
  #ive made a change
# i just commited a branch
    Operations = "Add Subtract Multiply Divide"
    print(Operations)
    user_input = input()
    if user_input == "Add" or user_input == "add":
        print("Input the two values to be added(separate with a space):")
        user_input = input()
        numbers = user_input.split()
        y = 0
        for i in numbers:
          numbers[y]  = int(i)
          y +=  1
        print(numbers[0] + numbers[1])
        continue
    elif user_input == "Subtract" or user_input == "subtract":
        print("Input the two values to be subtracted(separate with a space):")
        user_input = input()
        numbers = user_input.split()
        y = 0
        for i in numbers:
          numbers[y]  = int(i)
          y +=  1
        print(numbers[0] - numbers[1])
        continue
    elif user_input == "Multiply" or user_input == "multiply":
        print("Input the two values to be multiplied(separate with a space):")
        user_input = input()
        numbers = user_input.split()
        y = 0
        for i in numbers:
          numbers[y]  = int(i)
          y +=  1
        print(numbers[0] * numbers[1])
        continue
    elif user_input == "Divide" or user_input == "divide":
        print("Input the two values to be divided(separate with a space and divisor last):")
        user_input = input()
        numbers = user_input.split()
        y = 0
        for i in numbers:
          numbers[y]  = int(i)
          y +=  1
        print(numbers[0] / numbers[1])
        continue
    else:
        print("Cant perform operation!!")
        continue