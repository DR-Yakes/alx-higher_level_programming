#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, subtract, multiply, divide
a = 10
b = 5

result_add = add(a, b)
result_subtract = subtract(a, b)
result_multiply = multiply(a, b)
result_divide = divide(a, b)

print("Addition of {} and {} is {}".format(a, b, result_add))
print("Subtraction of {} from {} is {}".format(b, a, result_subtract))
print("Multiplication of {} and {} is {}".format(a, b, result_multiply))
print("Division of {} by {} is {}".format(a, b, result_divide))
