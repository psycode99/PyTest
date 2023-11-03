def add(x, y):
    return x + y


def divide_zero(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        return 'cannot be divided by zero'
    except TypeError:
        return 'please input integers'
    else:
        return result
    

def divide(x,y):
    return x / y