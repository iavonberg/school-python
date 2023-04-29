def my_function(num1, num2, num3=None):
    if num3 is not None:
        return (num1 + num2 + num3)/3
    else:
        return (num1 + num2)
    
print(my_function(1,2))
print(my_function(1,2,3))
