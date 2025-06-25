class Person: 
    def printdata(self):
        print(f"Name is {self.name}")
        print(f"Occupation is {self.occupation}")
        print(f"Network is {self.network}")

a=Person()
a.name="Ayaan"   
a.occupation="Software Dev" 
a.network=234
print(a.name,a.occupation,a.network)    

b=Person()
b.name="Amaar"   
b.occupation="Software" 
b.network=234456
print(b.name,b.occupation,b.network)
a.printdata()
b.printdata()