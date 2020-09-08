import time

def show_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        t = t2 - t1
        print("Total runtime: {}".format(t))
        return result
    
    return wrapper

@show_time
def fff(nums):
    return sum([i for i in range(nums)])

print(fff(1000000))