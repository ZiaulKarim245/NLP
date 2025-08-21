def math_operation(num1, num2, num3, operation):
    def addition(num1, num2, num3):
        return num1 + num2 + num3
    def subtraction(num1, num2, num3):
        return (num1 - num2) - num3
    def multiplication(num1, num2, num3):
        return (num1 * num2) * num3
    def division(num1, num2, num3):
        return (num1 / num2) / num3
    if operation == 'add':
        return addition(num1, num2, num3)
    elif operation == 'subtract':
        return subtraction(num1, num2, num3)
    elif operation == 'multiply':
        return multiplication(num1, num2, num3)
    else:
        return division(num1, num2, num3)
num1 = int(input())
num2 = int(input())
num3 = int(input())
operation = input()
result = math_operation(num1, num2, num3, operation)
print(f"The result of operation {operation} on {num1}, {num2} and {num3} is: {result}")