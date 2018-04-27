def call_count(counter):
    def decorator(function):
        def wrapper(*args, **kwargs):
            counter[0] += 1
            return function(*args, **kwargs)
        return wrapper
    return decorator


counter = [0]
@call_count(counter)
def somar(x, y):
    return x+y


for i in range(5):
    print("Soma {}: {}".format(counter[0], somar(i, i+1)))
