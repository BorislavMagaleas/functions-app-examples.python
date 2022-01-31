## Functions for data processing
## - lists, dicts, tuple, set | json, xml
def selectNumbers( pos_to_zero, vector ):
    if type(vector) != list and type(vector) != dict and type(vector) != tuple and type(vector) != set:
        print("ERROR: selectPositive works only with lists/dicts/tuples/sets !!!")
        return
    res_vector = []
    if pos_to_zero == "positive":  
        for v in vector:    # this is NOT for ... in range()
            if v >= 0:
                res_vector.append(v)

        return res_vector
    elif pos_to_zero == "negative":
        for v in vector:
            if v < 0:
                res_vector.append(v)

        return res_vector


####################################################
########## NUMERIC DATA ############
integers = [ -5, 0, 5, 10, -10, 15 ]
data = True
print( selectNumbers( "negative", integers ) )
print( selectNumbers( "positive", integers ) )

