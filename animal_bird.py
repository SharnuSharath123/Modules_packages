# approach 1
import animal
import bird

animal.fly()
animal.color()

bird.fly()
bird.color()

# approach 2
from animal import *
fly()
color()

from bird import *
fly()
color()