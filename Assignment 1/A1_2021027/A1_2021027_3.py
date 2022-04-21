degree = int(input("Degree of the polynomial: "))
coefficients = [int(input(f"Coefficient of x^{i}: "))
                for i in range(degree, -1, -1)]
lower_bound = int(input("lower bound: "))
upper_bound = int(input("upper bound: "))
increment = float(input("increment step: "))


def f(x):
    # Returns the value of f(x)
    index = 0
    value = 0
    while index <= degree:
        for i in range(degree, -1, -1):
            value += coefficients[index] * (x ** i)
            index += 1
    return value


# If the value of the function is negative in the given interval, save the least val of the function so that I can move the output graph towards right by that many units.
max_negatives = 0
x = lower_bound
while x <= upper_bound:
    val = round(f(x))
    if val < 0:
        if val < max_negatives:
            max_negatives = val
    x += increment
max_negatives = abs(max_negatives)

# Draw the graph
x = lower_bound
print('\n-----------------\n')
while x <= upper_bound:
    value = round(f(x))
    if value >= 0:
        print(f"{' '*max_negatives}|{'*'*value}")
    else:
        value = abs(value)
        print(f"{' '*(max_negatives-value)}{'*'*value}|")
    x += increment
