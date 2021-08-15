class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

    # def eat(self):
    #     print("eating")

    # def eat(self, food):
    #     print(f'eating {food}')

# common interface
def bird_fly(bird):
    bird.fly()

def bird_swim(bird):
    bird.swim()

#instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
bird_fly(blu)
bird_fly(peggy)

bird_swim(blu)
bird_swim(peggy)
