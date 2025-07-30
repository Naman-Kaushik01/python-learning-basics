info={
       144:"Naman",
       145:"Abhisek",
       146:"Jitesh",
       147:"Vivek",
       148:"Rahul"
}
print(info)
print(info[147])
print(info.get(144))

abt={"Name":"Naman","Age":18,"Eligible":True}
print(abt)
print(abt.values())
print(abt.keys())

for key in abt.keys():
    print(f"The Value Corresponding to {key} is {abt[key]}")