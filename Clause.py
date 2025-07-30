def fuunc1():
    try:
        l=[1,5,6]
        i=int(input("Enter The Index"))
        print(l[i])
        return 1
    except:
        print("Some Error Occured")
        return 0
    finally:
        print("Thank You Have A Good Day")

print (fuunc1())