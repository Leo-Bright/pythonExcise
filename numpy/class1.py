import numpy as np

def calAverage(array):
    assert type(array) is type([]), "input values is not list/array !"
    average = np.average(array)
    print(average)
    print(array)



a = [1,2,3,4,5,6,7,8,9,10]
calAverage(a)