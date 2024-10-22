#decorator
def greet(fx):
    print("hello welcome to the census")
    fx()
    print("thanks for using")
@greet
class person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def info(self):
        print(f"{self.name} is  {self.age} years old")
    
p1=person("garv",18,"male")
p1.info()