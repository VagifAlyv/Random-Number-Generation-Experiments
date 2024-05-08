
import numpy as np
import random
from matplotlib import pyplot as plt

# Experiment 1
ar_A = []
ar_B = []
ar_C = []
ar_X = []

av_A = []
av_B = []
av_C = []
av_X = []
vr_X = []


sum_A = []
sum_B = []
sum_C = []
sum_X = []

def generate_num():
    a = int(random.random() * 6) + 1
    b = int(random.random() * 4) + 1
    c = 2 * int(random.random() * 2) - 1
    x = a + (b * c)
    ar_A.append(a)
    ar_B.append(b)
    ar_C.append(c)
    ar_X.append(x)

    sum_A.append((sum_A[-1] + a) if len(sum_A) > 0 else a)
    sum_B.append((sum_B[-1] + b) if len(sum_B) > 0 else b)
    sum_C.append((sum_C[-1] + c) if len(sum_C) > 0 else c)
    sum_X.append((sum_X[-1] + x) if len(sum_X) > 0 else x)

    av_A.append((sum_A[-1]) / len(sum_A) if len(av_A) > 0 else a)
    av_B.append((sum_B[-1]) / len(sum_B) if len(av_B) > 0 else b)
    av_C.append((sum_C[-1]) / len(sum_C) if len(av_C) > 0 else c)
    av_X.append((sum_X[-1]) / len(sum_X) if len(av_X) > 0 else x)

    vr_X.append(sum((xi - av_X[-1]) ** 2 for xi in ar_X) / len(ar_X) if len(vr_X) > 0 else 0) 

for i in range(1, 30001):
    generate_num()

plt.figure()
plt.hist(ar_A,6,range=(1,7),align='left',density=True, rwidth=0.8)
plt.figure()
plt.hist(ar_B,4,range=(1,5),align='left',density=True, rwidth=0.8)
plt.figure()
plt.hist(ar_C,3,range=(-1,2),align='left',density=True, rwidth=0.8)
plt.figure()
plt.hist(ar_X,14,range=(-3,11),align='left',density=True, rwidth=0.8)


plt.figure()
plt.title("Average of A")
plt.plot(av_A)
plt.figure()
plt.title("Average of B")
plt.plot(av_B)
plt.figure()
plt.title("Average of C")
plt.plot(av_C)
plt.figure()
plt.title("Average of X")
plt.plot(av_X)
plt.figure()
plt.title("Variance of X")
plt.plot(vr_X)


# Experiment 2
# Part a (Inverse Transform Method)
U = []
Xa = []
av_Xa = []
vr_Xa = []


sum_Xa = []
sum_Xa_squared = 0 
n = 0

def generate_num():
    global sum_Xa_squared, n
    
    u = random.random()
    U.append(u)

    x = u ** (1/2)
    Xa.append(x)

    n += 1
    sum_Xa.append((sum_Xa[-1] + x) if len(sum_Xa) > 0 else x)
    av_Xa.append(sum_Xa[-1] / n)

    sum_Xa_squared += x ** 2

    if n > 1:
        variance = (sum_Xa_squared - (sum_Xa[-1] ** 2) / n) / (n - 1)
    else:
        variance = 0
    
    vr_Xa.append(variance)

for i in range(1, 30001):
    generate_num()

plt.figure()
for i in range(len(Xa)):
    plt.plot([Xa[i],U[i]],[1,1.2])
plt.figure()
hU = plt.hist(U,100,alpha=0.5,density=True)
hXa = plt.hist(Xa,100,alpha=0.5,density=True)
plt.figure()
plt.plot(np.cumsum(hU[0]))
plt.plot(np.cumsum(hXa[0]))


plt.figure()
plt.title("Average of Xa")
plt.plot(av_Xa)
plt.figure()
plt.title("Variance of Xa")
plt.plot(vr_Xa)


# Part b (Rejection Method)
Xb = []
av_Xb = []
vr_Xb = []


sum_Xb = []
sum_Xb_squared = 0 
n = 0

def generate_num():
    global sum_Xb_squared, n
  
    # The density function is f(x) = 2x
    x = random.random()
    u = random.random()

    
    
    if (2 * x >= 2 * u):
        n += 1
        Xb.append(x)
        sum_Xb.append((sum_Xb[-1] + x) if len(sum_Xb) > 0 else x)
        av_Xb.append((sum_Xb[-1]) / n)

        sum_Xb_squared += x ** 2
        if n > 1:
            variance = (sum_Xb_squared - (sum_Xb[-1] ** 2) / n) / (n - 1)
        else:
            variance = 0
    
        vr_Xb.append(variance)

for _ in range(30000):
    generate_num()


plt.figure()
hXb = plt.hist(Xb,100,density=True)
plt.figure()
plt.plot(np.cumsum(hXb[0]))

plt.figure()
plt.title("Average of Xb")
plt.plot(av_Xb)
plt.figure()
plt.title("Variance of Xb")
plt.plot(vr_Xb)

plt.show()



