import math
# 1. Max of two function
def max (x,y):
    if x>=y: return x
    else: return y
# print(max(5,8))

# 2. fizz_bizz function
def fizz_buzz(x):
    if x%3==0 and x%5==0: return "FizzBuzz"
    elif x%3==0: return "Fizz"
    elif x%5==0: return "Buzz"
    else: return x
# print(fizz_buzz(16))

# 3. Speed checking function
def speed_check(speed):
    if speed<=70: print("Ok")
    elif speed>70:
        overSpeed = speed-70
        points = math.floor(overSpeed/5);
        if points>=12: print("License Suspended")
        else: print("Points:",points)
# speed_check(77)

# 4. Show Numbers
def show_numbers(limit):
    for i in range(limit+1):
        if i%2==1: print(i,"ODD")
        else: print(i,"Even")
# show_numbers(4)