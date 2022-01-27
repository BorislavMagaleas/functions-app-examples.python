## Functions for data processing
## - lists, dicts, tuple, set | json, xml
## 1. receives a vector of ints, returns a vector of positive ints 
def selectPositive( vector ):
    if type(vector) != list and type(vector) != dict and type(vector) != tuple and type(vector) != set:
        print("ERROR: selectPositive works only with lists/dicts/tuples/sets !!!")
        return
    pos_vector = []
    for v in vector:    # this is NOT for ... in range()
        if v >= 0:
            pos_vector.append(v)

    return pos_vector

## 2. receives a vector of ints, returns a vector of negative ints
def selectNegative( vector ):
    if type(vector) != list and type(vector) != dict and type(vector) != tuple and type(vector) != set:
        print("ERROR: selectNegative works only with lists/dicts/tuples/sets !!!")
        return
    neg_vector = []
    for v in vector:
        if v < 0:
            neg_vector.append(v)

    return neg_vector


####################################################
########## NUMERIC DATA ############
integers = [ -5, 0, 5, 10, -10, 15 ]
data = True
print( selectPositive( integers ) )
print( selectNegative( integers ) )

