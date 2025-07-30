def gMean(a , b):
    mean=(a+b)/(a*b)
    print(mean)
def Sub(a , b):
    Sub=a-b
    print(Sub)
def Compare(a , b):
    if(a>b):
        print("a is greater")
    else:
        print("b is greater")
a=8
b=9
gMean(a,b)
Sub(a,b)

Compare(a,b)

def Naman(a , b):
    sum=a+b
    print(sum)

a=55
b=100
Naman( a , b)


#FUNCTION ARGUMENTS 

# 1 DEFAULT ARGUMENTS
def avgerage(a=9,b=11):
    print("The Average is : ",(a+b)/2)

avgerage(b=9)


def name(fname,Mname="Kaushik",lname="Pandey"):
    print("Namaskar",fname,Mname,lname)

name("Naman","kumar","Dubey")

#2 KEYWORD ARGUMENTS

def name(fname,mname,lname):
    print("Hello",fname,mname,lname)

name(mname="Peter",fname="jade",lname="Whatson")

# VARIABLE LENGTH ARGUMENTS

def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
        print("Average is : ",sum/len(numbers))

average(3,4)