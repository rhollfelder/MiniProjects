# Calculator idea from Kyle
# Be able to take 2 inputs and perform a basic function (*/-+)
print('This calculator takes two inputs and performs a basic operation.')
# input 1
a = input('First value: ')
# input 2
b = input('Second value: ')

out = [a + b, a - b, a * b, a / b]

# operator
print('For the operation, choose:')
print('1 - addition')
print('2 - subtraction')
print('3 - multiplication')
print('4 - division')
print('5 - all')
op = input('Function to perform: ')
op -= 1
if op == 4:
    print('a + b = ' + str(out[0]))
    print('a - b = ' + str(out[1]))
    print('a * b = ' + str(out[2]))
    print('a / b = ' + str(out[3]))
elif 0 <= op <= 3:
    print('Answer = ' + out[op])
else:
    print('Invalid Selection')
