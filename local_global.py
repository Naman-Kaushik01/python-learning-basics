x=19 #Global variable

def my_function():
    global x
    x=10
    y=5 #local variable
    print(y)

my_function()
print(x)
print(y) #This Will cause an error because y is local variable and not accessibple outside the function