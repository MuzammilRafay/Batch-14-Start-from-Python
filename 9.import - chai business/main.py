#Method 1
import recipes.flavor
print(recipes.flavor.elachai_chai())


#Method 2
from recipes.flavor import elachai_chai,ginger_chai
print(elachai_chai())
print(ginger_chai())


#Method 3
from recipes.flavor import elachai_chai as chai
print(chai())


#Method 4 (Bad paractice)
from recipes.flavor import *
print(elachai_chai())
print(ginger_chai())


#Method 5
import recipes.flavor as flavors
print(flavors.elachai_chai())
print(flavors.ginger_chai())