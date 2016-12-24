import matplotlib.pyplot as plt
import random


def plot_(arr, n=100):
    y = [0] * n
    for i in range(n):
        for j in range(len(arr)):
            y[i] += arr[j] * pow(i, j)
    plt.plot(y)


def cost_fn(m, x, y, theta1, theta0=0):
    cost = 0
    costs = [0]*m
    for i in range(m):
        costs[i]=cost
        cost += pow((hypothesis_fn(theta1, theta0, x[i]) - y[i]), 2)
    return (1 / 2 * m) * cost


def hypothesis_fn(theta1, theta0, x):
    return theta1 * x + theta0


X = [i for i in range(10)]
Y = [2 * X[i] + 1 for i in range(10)]
m = len(X)
alpha = 0.1  # Learning rate

theta1 = random.randint(-100, 100)

n = 100

costs = []

while (cost_fn(m, X, Y, theta1) >= 0 and n>0):

    # calculate partial derivative
    pd = 0
    for i in range(m):
        pd += hypothesis_fn(theta1, 0, X[i]) - Y[i]
    pd /= m

    n -= 1

    theta1=theta1-alpha*pd

    costs.append(cost_fn(m, X, Y, theta1))

print(theta1, 'cost = ', cost_fn(m, X, Y, theta1))

#plotting the graph

plt.subplot(221)

plot_([0, theta1])
plt.plot(X, Y, 'ro')
plt.axis([0, 1.2*X[-1], 0, 1.2*Y[-1]])

plt.subplot(222)
plt.plot(costs)

plt.show()