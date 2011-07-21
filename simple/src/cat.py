'''Simple example defining a Cat class, and instantiating a cat from it'''

class Cat(object):
    def meow(self):
        print("Meow!")

    def eat(self):
        print("Glub glub glub")
        
cat = Cat()
cat.meow()
cat.eat()
    