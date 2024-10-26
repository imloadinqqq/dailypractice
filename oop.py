class Dog:
    response = "woof"
    
    def bark(self):
        print(self.response)
        
class Cat:
    response = "meow"
    
    def meow(self):
        print(self.response)
        
class Student:
    id = 1
    gpa = 0
    name = ""
    
    def setId(self, new_id):
        self.id = new_id
        
    def setGPA(self, new_gpa):
        self.gpa = new_gpa
        
    def setName(self, new_name):
        self.name = new_name
        
    def getId(self):
        return self.id
    
    def getGPA(self):
        return self.gpa
    
    def getName(self):
        return self.name
    
    def toString(self):
        return "ID: " + str(self.id) + "\nName: " + self.name + "\nGPA: " + str(self.gpa)
    
    
student = Student()
student.setId(1)
student.setGPA(3.6)
student.setName("Alex")

print(student.toString())

dog = Dog()
cat = Cat()

dog.bark()
cat.meow()