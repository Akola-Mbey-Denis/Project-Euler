# Even Fibonacci numbers
   
# Problem 2

# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
from itertools import takewhile

def fibonacci():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a+b


def even(it):
    for n in it:
        if n % 2 == 0:
            yield n

if __name__=="__main__":
    print(sum(takewhile(lambda f: f <= 4000000, even(fibonacci()))))