import sys
import argparse
import time
import threading
import unittest
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from multiprocessing import Pool
import multiprocessing

def f(n):
    sum = 0 
    for x in range(1000):
        sum += x * x
    return sum

if __name__ == "__main__":
    array = [1,2,3,4,5]
    t1 = time.time()
    p = Pool()
    result = p.map(f,range(10000))
    p.close()
    p.join()
    for n in array:
        result.append(f(n))
    print(result)
    print("pool took ", time.time()-t1)

def deposit(balance):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()

def withdraw(balance):
    for j in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()

result = []

def calc_square(numbers):
    for n in numbers:
        result.append(n*n)
    print("Done Inside! " + str(result))

def calc_cube(numbers):
    for m in numbers:
        time.sleep(5)
        print("cube " + str(m * m * m))

if __name__ == "__main__": 
    balance = multiprocessing.Value('i',200)
    lock = multiprocessing.Lock()
    d = multiprocessing.Process(target=deposit, args=(balance,))
    w = multiprocessing.Process(target=withdraw, args=(balance,))
    d.start()
    w.start()
    d.join()
    w.join()
    print(balance.value)
    arr = [2,3,8,9]
    result = multiprocessing.Array('i', 3)
    value = multiprocessing.Value('d', 0.0)
    p1 = multiprocessing.Process(target=calc_square, args=(arr,result))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

def calc_square(numbers):
    print("Calculate Square of Numbers")
    for n in numbers:
        time.sleep(0.2)
        print("Square", n * n)

def calc_cube(numbers):
    print("Calculate Cube of Numbers")
    for m in numbers:
        time.sleep(0.2)
        print("Cube", m * m * m)

arr = [2,3,8,9]
t = time.time()
t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()
t1.join()
t2.join()
print("{0} seconds to execute".format(time.time()-t))

try:
    html = urlopen("https://abcxyz.com")
except HTTPError as e:
    print("HTTP error")
except URLError as e:
    print("Server not found!")
else:
    print(html.read())
    
try:
    html = urlopen("http://www.example.com/")
except HTTPError as e:
    print("HTTP error")
except URLError as e:
    print("Server not found!")
else:
    print("HTML Details")    
    print(html.read())  


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end-start)*1000) + "mil sec")
        return result
    return wrapper

@time_it
def calc_square(numbers):
    start = time.time()
    result = []
    for number in numbers:
        result.append(number * number)
    end = time.time()
    print("Time Taken: {0} mil sec".format(str((end-start)*1000)))
    return result

@time_it
def calc_cube(numbers):
    start = time.time()
    result = []
    for number in numbers:
        result.append(number * number * number)
    end = time.time()
    print("Time Taken: {0} mil sec".format(str((end-start)*1000)))
    return result

array = range(1,100000)
out_square = calc_square(array)
out_cube = calc_cube(array)

if __name__ == "main":
    parser = argparse.ArgumentParser()
    parser.add_argument("number1", help="first number")
    parser.add_argument("number2", help="second number")
    parser.add_argument("operation", help="operation")
    args = parser.parse_args()
    print(args.number1)
    print(args.number2)
    print(args.number3)






