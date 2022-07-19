import math
# 1. Max of two function
import random


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

# 5. Sum of multiples
def sum_of_multiples(limit):
    sum=0;
    for i in range(limit+1):
        if i%3==0 or i%5==0:
            sum=sum+i
    return sum
# print(sum_of_multiples(10))

# 6. show_stars
def show_stars(rows):
    for i in range (1,rows+1):
        print("*"*i)
# show_stars(5)

# 7. prime number
def isPrime(number):
    count=0
    for i in range(1,number):
        if number%i==0: count = count+1
    if count==1: return True
    else: return False
# print(isPrime(7))
def prime_numbers(limit):
    for i in range(1,limit+1):
        if isPrime(i):
            print(i)
# print(prime_numbers(5))

def roll():
    print(f"({random.randint(1,6)},{random.randint(1,6)})")
roll()