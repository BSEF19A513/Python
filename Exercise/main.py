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