#Print numbers from 0 to 100
#numbers multiples of 3 print Buzz
#Numbers multiples of 5 print Fizz
#Numbers multiples by both print FizzBuzz

for x in range(1,101):
    if x % 3 ==0 and x % 5 ==0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Buzz")
    elif x % 5 == 0:
        print("Fizz")
    else:
        print(x)
        