import numpy as np
from cnis import statistic as st

def methodA(xArray):
    x_ = st.calMedian(xArray)
    s_ = st.calMADe(xArray)
    while True:
        delta = 1.5 * s_;
        for index in range(xArray.size):
            if xArray[index] < (x_ - delta):
                xArray[index] = (x_ - delta)
            elif xArray[index] > (x_ + delta):
                xArray[index] = (x_ + delta)
            else:
                pass
        newX_ = xArray.sum()/xArray.size
        newS_ = 1.134 * np.sqrt(((xArray - newX_)**2).sum()/(xArray.size - 1))
        if (newX_ == x_) and ((1000*newS_)%10 == (1000*s_)%10):
            break
        else:
            x_ = newX_
            s_ = newS_
    return [x_,s_]

def methodS(matrix):
    v = [[1.645,1.097],[1.517,1.054],[1.444,1.039],[1.395,1.032],[1.359,1.027],[1.332,1.024],[1.310,1.021],[1.292,1.019],[1.277,1.018],[1.264,1.017]]
    shape = matrix.shape
    eta = v[shape[1]-2][0]
    xi =  v[shape[1]-2][1]
    w = np.std(matrix,axis=1)
    w_ = st.calMedian(w)
    while True:
        psi = eta * w_
        for index in range(w.size):
            if w[index] > psi:
                w[index] = psi
            else:
                pass
        newW_ = xi * np.sqrt((w**2).sum()/shape[0])
        if((1000*w_)%10 == (1000*newW_)%10):
            break
        else:
            w_ = newW_
    return w_

def methodQn(array):
    d = []
    p = array.size
    for i in range(p-1):
        for j in range(i+1,p):
            d.append(abs(array[i]-array[j]))
    sortedD = np.sort(d)
    h = p//2
    k = h*(h-1)//2
    b = [0.9937,0.9937,0.5132,0.8440,0.6122,0.8588,0.6699,0.8734,0.7201,0.8891,0.7574]
    if p > 12:
        if p%2==1:
            rp = (1.6019+(-2.128-5.172/p)/p)/p
        else:
            rp = (3.6756+(1.956+(6.987-77/p)/p)/p)/p
        bp = 1/(rp+1)
    else:
        bp = b[p-2]
    Qn = 2.2219 * sortedD[k] * bp
    return Qn


a = np.array([1.1,1.2,2.1,3.1,3.6,5.6,6.1,7.4,8.4,9,1.8,6.6])
b = np.array([1,10,8,3,4,5,6,7,2,9,1])
mat = np.array([[1,10,8,3,4,5,6,7,2,9,1],[1,5,8,3,4,7,6,7,2,9,4],[3,10,9,3,4,1,6,7,4,9,11]])

print(methodA(a))
# print(methodS(mat))
print(methodQn(a))
