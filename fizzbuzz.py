# Looping through every number from 1-100
for x in range(1,101):
    # ternary operator to handle printing "Fizz", "Buzz" or "FizzBuzz" if x is a multiple of 3 or 5
    print("FizzBuzz") if x % 3 == 0 and x % 5 == 0 else print("Fizz") if x % 3 == 0 else print("Buzz") if x % 5 == 0 else print(x)