# approach 1
import x
import y

obj1 = x.Animal()
obj1.fly()
obj1.color()

obj2 = y.Bird()
obj2.fly()
obj2.color()


# approach 2
from x import Animal
from y import Bird

obj1 = Animal()
obj1.fly()
obj1.color()

obj2 = Bird()
obj2.fly()
obj2.color()