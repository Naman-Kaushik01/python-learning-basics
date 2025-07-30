# FINDING FACTORIAL OF A NUMBER 
def factorial(n):
    if(n==1 and n==0):
        return 1
    else:
        return n * factorial(n-1)
    
n=int(input("Enter Any Number"))
print("Your Number is :",n)
print(factorial(n))