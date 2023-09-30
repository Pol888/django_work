def f(n):
    f.__dict__['1'] = 3
    return [1, 2, n]






print(len(f.__dict__))

