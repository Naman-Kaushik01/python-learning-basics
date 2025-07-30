#DEFAULT CONSTRUCTOR

class Details:

    def __init__(self,name,occ):
        self.name=name
        self.occ=occ
        print("Hey I am a Person")

    def info(self):
        print(f"{self.name} is a {self.occ}")

a= Details("Naman","Youtuber")
b= Details("Abhisek","Cricketer")

a.info()
b.info()
