a=input("Enter The Number : ")
print(f"Multiplication Table of {a} is : ")
try:
    for i in range(1,11):
        print(f"{int(a)}X{i}={int(a)*i}")

except:
    print("Invalid Input !!")