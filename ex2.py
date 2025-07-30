time=int(input("Enter the time"))
#name=input("ENTER YOUR NAME")
if(time<=1 & time<12):
    print("Good Morning...",name)
elif(time<=12 & time<17):
    print("Good Afternoon",name)

elif(time<=17 & time<20):
    print("Good Evening",name)
elif(time<=20 & time<=24):
    print("Good Night",name)
else:
    print("INVALID INPUT")