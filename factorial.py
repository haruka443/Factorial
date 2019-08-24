factorial = float(input('Give a number: '))
result = 1
i = 1
while i <= factorial:
    result = result * i
    i += 1
print(result)

#def factorial(number):
#    if number > 1:
#        return number*factorial(number - 1)
#    elif number in (0,1):
#        return 1
#    if number < 0:
#        print('It's not possible to perform this operation')

#print(f'The factorial {number: .0f} is {factorial(number): .0f}')