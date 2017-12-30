import numpy as np

def calAverage(array):
    average = np.average(array)
    return average;

def calMedian(array):
    median = np.median(array)
    return median

def calVariance(array):
    variance = np.var(array)
    return variance

def calStandardVar(array):
    standardVar = np.std(array)
    return standardVar

def calQuantile3(array):
    quantile3 = np.percentile(array,75, interpolation='nearest')
    return quantile3

def calQuantile1(array):
    quantile3 = np.percentile(array,25, interpolation='nearest')
    return quantile3

def calIQR(array):
    return calQuantile3(array) - calQuantile1(array)

def calNIQR(array):
    return 0.7413 * calIQR(array)

def calMADe(array):
    media = calMedian(array);
    if type(array) is type(np.array([])):
        d = abs(array - media)
    elif type(array) is type([]):
        d = []
        for num in array:
            d.append(abs(array - media))
    return 1.483 * calMedian(d)




def testVar(array):
    for ele in a:
        yield ((ele-5)**2)

a = np.array([0,10,8,3,4,5,6,7,2,9,1])
print(a)
print("average:",calAverage(a))
print("median:",calMedian(a))
print("variance:",calVariance(a))
print("standardVar:",calStandardVar(a))
print("quantile_3:",calQuantile3(a))
print("quantile_1:",calQuantile1(a))
print("IQR:",calIQR(a))
print("nIQR:",calNIQR(a))
print("MADe",calMADe(a))