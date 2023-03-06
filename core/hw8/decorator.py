def typed(t):
    def decorator(func):
        def wrapper(*args):
            args = list(args)
            for i in range(len(args)):
                if type(args[i]) != t:
                    if t == 'str':
                        args[i] = str(args[i])
                    elif t == 'int':
                        args[i] = int(args[i])
                elif type(args[i]) == 'float':
                    pass
            check_type = all(isinstance(arg, str) for arg in args)
            if check_type:
                return ''.join(args)
            else:
                return sum(args)

        return wrapper

    return decorator


@typed(t='str')
def add_two_symbols(a, b):
    return a + b


@typed(t='int')
def add_three_symbols(a, b, с):
    return a + b + с
