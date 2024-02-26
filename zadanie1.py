def apple_twice(func, value):
    return func(func(value))

result = apple_twice(lambda x: x +2, value=10 )
print(result)
