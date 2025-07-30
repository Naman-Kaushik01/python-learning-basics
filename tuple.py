tup=(1,2,3,4,"Naman","Lakshya")
print(tup)
if "Naman" in tup:
    print("Yes Naman is Present")
else:
    print("Not availaible")

tup2=tup[1:4:2]
print(tup2)

#MANIPULATING TUPLES

countries=("India","Nepal","China","Japan","England")
temp=list(countries)
temp.append("Russia")
temp[2]="Finland"
countries=tuple(temp)
print(countries)

#WE CAN ALSO CONCATINATE TWO TUPLE
north=("Bihar","Uttar Pradesh","West Bengal")
south=("Tamil Nadu","Kerala","Kernatka")
print(north)
print(south)
india=north+south

print(india)