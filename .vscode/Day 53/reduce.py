from functools import reduce
#list of numbers
numbers=[1,2,3,4,5,6,7]
#calculate the sum using reduce function
sum=reduce(lambda x,y:x+y,numbers)
sub=reduce(lambda x,y:x-y,numbers)
mul=reduce(lambda x,y:x*y,numbers)
div=reduce(lambda x,y:x/y,numbers)
#print the sum
print(sum)
print(sub)
print(mul)
print(div)