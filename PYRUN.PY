class Fish:
    def type(self):
        print("fish")

class Shark(Fish):
    def type(self):
        print("shark")

# Create objects
obj_goldfish = Fish()
obj_hammerhead = Shark()

# Demonstrate method overriding
for obj in (obj_goldfish, obj_hammerhead):
    obj.type()
