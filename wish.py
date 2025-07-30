import time
hour=int(time.strftime('%H'))
name=input("Enter Your Name")

if(hour>=0 and hour<12):
    print("GOOD MORNING",name)
elif(hour>=12 and hour<17):
    print("GOOD AFTERNOON",name)
elif(hour>=17 and hour<20):
    print("GOOD EVENING",name)
elif(hour>20 and hour<0):
    print("GOOD NIGHT",name)