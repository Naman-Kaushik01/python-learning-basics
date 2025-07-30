info={"Naman",604,True,"Shubh"}
print(info)
print(type(info))

for item in info:
    print(item)

set=()
print(type(set))

#UNION AND UNION UPDATE
cities={"Patna","Motihari","Gaya","Muzzaaffarpur"}
cities1={"Chakia","Patna","Dhaka",}
print(cities)
print(cities1)
print ("The union is :",cities.union(cities1))
cities.update(cities1)
#print(cities)

#INTESECTION AND INTERSETION UPDATE
print("The Intersection is : ",cities.intersection(cities1))
print("The Symmetric difference is :",cities.symmetric_difference(cities1))
print("The difference is :",cities.difference(cities1))


#SET METHODS
s1={"a","b","c","d"}
s2={"e","f","g","d"}
print(s1.isdisjoint(s2))
s1.add("Naman")
print(s1)
print(s1.discard("b"))