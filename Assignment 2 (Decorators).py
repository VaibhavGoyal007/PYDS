import timeit

def timer(func):
    def inner(*args, **kwargs):
        if args==() and kwargs=={}:
            start_time = timeit.default_timer()
            func()
            elapsed = timeit.default_timer() - start_time
            print("Function '{name}' took {time} seconds to complete".format(name = func.__name__, time = elapsed))
            return func()
        elif args != () and kwargs == {}:
            start_time = timeit.default_timer()
            func(*args)
            elapsed = timeit.default_timer() - start_time
            print("Function '{name}' with positional arguments {positional} took {time} seconds to complete".format(name = func.__name__, positional = args, time = elapsed))
            return func(*args)
        elif args == () and kwargs != {}:
            start_time = timeit.default_timer()
            func(**kwargs)
            elapsed = timeit.default_timer() - start_time
            print("Function '{name}' with keyword arguments {keyword} took {time} seconds to complete".format(name = func.__name__, keyword = kwargs,time = elapsed))
            return func(**kwargs)
        elif args != () and kwargs != {}:
            start_time = timeit.default_timer()
            func(*args, **kwargs)
            elapsed = timeit.default_timer() - start_time
            print("Function '{name}' with positional arguments {positional} and keyword arguments {keyword} took {time} seconds to complete".format(name = func.__name__, positional = args, keyword = kwargs, time = elapsed))
            return func(*args, **kwargs)
    return inner

@timer
def function(a,b,c,f):
    return

function(3,4,c=5,f=3)