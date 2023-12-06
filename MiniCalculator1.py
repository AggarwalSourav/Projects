num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
def add_numbers(a, b):
    result = a + b
    return result
sum_result = add_numbers(num1, num2)
print("-> The sum is:", sum_result)

def sub_numbers(a, b):
    result = a - b
    print("-> The difference is:", result)
sub_numbers(num1, num2)

def mul_numbers():
    result = num1 * num2
    return result
mul_result = mul_numbers()
print("-> The product is:", mul_result)

def div_numbers():
    result = num1/num2
    print("-> The division is:", result)
div_numbers()
