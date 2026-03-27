'''
Assignment Name : Logic Builder
Description : Print numbers 1–50 with Fizz/Buzz logic and count occurrences using loops and functions.
'''
def fizzbuzz_count(start,end):
    fizzbuzz=0
    fizz=0
    buzz=0

    for i in range(start,end+1):
        if (i%3==0 and i%5 ==0):
            print("FizzBuzz")
            fizzbuzz+=1
        elif i%3 ==0:
            print("Fizz")
            fizz+=1
        elif i%5 ==0:
            print("Buzz")
            buzz+=1
        else:
            print(i)
    
    print("Counts\n")
    print("FizzBuzz",fizzbuzz)
    print("Fizz",fizz)
    print("Buzz",buzz)
fizzbuzz_count(1,50)