import time
from functools import lru_cache

@lru_cache(maxsize=128)

def slow_add(a, b):
    time.sleep(2)  
    return a + b

while True:
     a= int(input("Enter the First A number: "))
     b=int(input("Enter the Second B number:"))
     result= slow_add(a,b)
     print(f"The result of adding {a} and {b} is: {result}")    



       