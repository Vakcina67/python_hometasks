def val_checker(valid_func):
    def sub_val_checker(func):
        def wrapper(number):
            if valid_func(number):
                print(func(number))
            else:
                raise ValueError(f'wrong val {number}')

        return wrapper

    return sub_val_checker

@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

calc_cube(-4)