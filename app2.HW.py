## data processing - functions
from random import randint


## 3. generate a vector of random ints
def genIntVector(length = 5, min_val = -100, max_val = 100):
    vector = []
    for i in range(length):
        vector.append(randint(min_val,max_val))

    return vector



print( genIntVector( max_val = 0 ) )
