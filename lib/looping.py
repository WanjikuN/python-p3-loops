#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")
happy_new_year()
def square_integers(int_list):
    sqr_list= [i**2 for i in int_list]
    return sqr_list

def fizzbuzz():
    for i in range(100):
        # print(i+1)
        match((i+1)%3, (i+1)%5 ):
            case(0,0):
                print("FizzBuzz") 
            case(0,_):
                print("Fizz") 
            case(_,0):
                print("Buzz") 
            case _:
                print(i+1) 
fizzbuzz()