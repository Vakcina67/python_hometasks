def type_logger(func):
    def wrapper(*args):
        result = func(*args)
        res_list = [f'{arg}: {type(arg)}, {func.__name__}' for arg in args]
        print(', '.join(res_list))
        return result
    return wrapper

@type_logger
def calc_cube(*args):
    return [arg ** 3 for arg in args]

print(calc_cube(5, 6, 7))
