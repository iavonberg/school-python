
def example():
    x = 1
    y=3
    print(x+y)

    if x < y:
        print(x, 'is less than', y)

def main():
    example()

def addition(num1, num2):
    answer = num1 + num2
    return answer

x = addition(5,6)
print(x)

x = 6

def example2():
    z = 5
    print(z)

example2()

def example3():
    z = 7
    print(z)

    y = x + 1
    print(y)

example3()

def example4():
    global x
    x+= 1
    print(x)

example4()