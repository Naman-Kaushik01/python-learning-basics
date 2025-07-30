f=open('myfile.txt','r')
text=f.read()
print(text)
f.close()

#WRITTING TO A FILE

f=open('myfile2.txt','w')
f.write("Hello World!\n")
f.close()

#APPEND 

f=open('myfile2.txt','a')
f.write("How are You Doing Now\n I am in Full Fun\n")
f.close()

# THE WITH STATEMENT

with open('myfile2.txt','a') as f:
    f.write("Hey I am Learning Python\n ")

#THE  readlines() METHOD

f=open('myfile.txt','r')
while True:
    line=f.readlines()
    if not line:
        break
    print(line)


f=open('marks.txt','r')
i=0
while True:
    i=i+1
    line=f.readline()
    if not line:
        break
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]

    print(f"Marks of Student{i} in maths is :{m1}")
    print(f"Marks of Student{i} in maths is :{m2}")
    print(f"Marks of Student{i} in maths is :{m3}")

    print(line)

#WRITELINES METHOD

f=open('myfile3.txt','w')
lines=['line 1\n','line2\n','line3\n']
f.writelines(lines)
f.close()

