class person:
    name="Naman"
    age=18
    proffesion="Software Developer"
    Networth=10
    def info(self):
        print(f"Hello Eveyone ! I am {self.name} My Age is {self.age} I am a {self.proffesion}")

a=person()
b=person()
a.name="Abhisek"
a.age=19
b.name="Nitesh"
b.proffesion="Accountant"

#print(a.name,a.proffesion)
a.info()
b.info()