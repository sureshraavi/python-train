def increment_by_one(number):
    return number + 1

# if a function can fit in one line, you can replace it with a lambda (a nameless function)

assert (lambda x: x + 1)(2) == 3

assert (lambda x: x + 1)(2) == increment_by_one(2)

assert (lambda x, y: x + y)(10, 20) == 30

# lambda is very new and very trendy (good to know as you need to understand lambda in a program)
