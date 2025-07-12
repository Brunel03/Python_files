import time

def duration(func):
    def wrapper(*args):
        s_time = time.time()
        func(*args)
        e_time = time.time()
        print(f"Function '{func.__name__}' took {e_time - s_time:.2f} seconds to be execute.")
    return wrapper



# Multiplication table with generator
#@duration
def multi_table(num,ran):
    for i in range(1, ran+1):
        yield str(num)+" x "+str(i)+" = "+ str(num*i)

for element in multi_table(14,1000):
    print(element)
#multi_table(14,10000)
#"""
@duration
def print_table(number,b):
    for i in range (1,b+1):
        print(f"{number} x {i} = {number*i}")

print_table(12,10000)
#"""