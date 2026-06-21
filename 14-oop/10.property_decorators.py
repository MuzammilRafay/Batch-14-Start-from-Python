class TeaLeaf:
    def __init__(self, age):
        self._age = age

    @property #isko ap batare ho ye ye chiz _age hai 
    def age(self):
        return self._age + 2
    
    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Tea leaf age must be between 1 and 5 years")
        
leaf = TeaLeaf(2)
print(leaf.age) #isme ek chiz ap note karien leaf.age()
leaf.age = 6
print(leaf.age)
