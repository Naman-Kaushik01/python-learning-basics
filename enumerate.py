marks=[12,56,32,45,98,99,45,43]
# index=0
# for mark in marks:
#     print(mark)
#     if(index==5):
#         print("well Done !")
#     index+=1

#TO ENUMERATE THIS PROBLEM 
for index, mark in enumerate(marks):
    print(mark)
    if (index==5):
        print("Well Done! Keep it up..")

#CHANGING THE START INDEX
        
fruits=['apple','bananaa','mango','guava','orange']
#print(type(fruits))

for index, fruits in enumerate(fruits,start=1):
    if(index==3):
        print("King of All Fruits")
    print(index,fruits)
