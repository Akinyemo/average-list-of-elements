#Finds average given x is a list of values
def calc_average(x):
    if isinstance(x,list) == False:
        raise TypeError('This is not an list')

    if len(x) < 1:
        raise ValueError('This list is empty')

    sum = 0
    for i in x:
        sum = sum + i

    #if isinstance(sum,int) == False:  #not sure how I would check this short of checking all elements in list
        #if isinstance(sum,float) == False:
            #raise ValueError('This list is not an integer or deciml')
    sum = sum / len(x) 
    return(sum)
