'''
Description: 
Author: Jackeeee_M
Date: 2022-10-05 19:28:42
LastEditors: Jackeeee_M
LastEditTime: 2022-10-05 23:26:32
'''

import numpy as np
import math
from fastprogress import progress_bar
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

SIZE = 100
MAX_EPOCH = 5000
c1 = 1
c2 = 1
X = []
P = []
F = []
V = []
P_BEST = []

def draw_3D():
    fig = plt.figure()
    ax3 = plt.axes(projection='3d')

    xx = np.arange(-500,500,0.1)
    yy = np.arange(-500,500,0.1)
    X, Y = np.meshgrid(xx, yy)
    Z = (-X)*np.sin(np.sqrt(abs(X))) + (-Y)*np.sin(np.sqrt(abs(Y)))

    ax3.plot_surface(X,Y,Z,cmap='rainbow') 
    plt.title("Schwefels function")
    plt.xlim((-500, 500))
    plt.ylim((-500, 500))
    plt.xlabel('x1')
    plt.ylabel('x2')

def draw(X,epoch):
    xc = []
    yc = []
    for i in range(SIZE):
        xc.append(X[epoch][i][0])
        yc.append(X[epoch][i][1])
    xc = np.array(xc)
    yc = np.array(yc)
    
    plt.scatter(xc,yc,s=4)
    # set the title
    plt.title("EPOCH {i}".format(i=epoch))
    plt.xlim((-500, 500))
    plt.ylim((-500, 500))
    plt.xlabel('x1')
    plt.ylabel('x2')


def function(x):
    f = (-x[0])*math.sin(math.sqrt(abs(x[0]))) + (-x[1])*math.sin(math.sqrt(abs(x[1])))
    return f

def limit(x):
    for i in range(2):
        if x[i] > 500:
            x[i] = 500
        elif x[i] < -500:
            x[i] = - 500
    return x



if __name__ == '__main__':
    # set the seed
    rnd = np.random
    rnd.seed(1120192001)

    # generate particle randomly in [-500,500]
    x1 = (rnd.rand(SIZE)*1000-500).tolist()
    y1 = (rnd.rand(SIZE)*1000-500).tolist()
    
    # initialize the initial state of EPOCH 0
    X.append(list(map(np.array,zip(x1,y1))))
    P.append(list(map(np.array,zip(x1,y1))))
    v = [np.array([0,0])] * SIZE
    V.append(v)
    f = []
    for s in range(SIZE):
        f.append(function(X[0][s]))
    F.append(f)
    P_BEST.append(P[0][F[0].index(max(F[0]))])

    # iter
    for epoch in progress_bar(range(MAX_EPOCH)):
        x = []
        v = []
        f = []
        p = []
        # for particles in one EPOCH
        for s in range(SIZE):
            # random in [0,1]
            r1 = rnd.uniform()
            r2 = rnd.uniform()
            # calculate the new state
            v_new = V[epoch][s] + c1*r1*(P[epoch][s] - X[epoch][s]) + c2*r2*(P_BEST[epoch] - X[epoch][s])
            x_new = X[epoch][s] + v_new
            # limit
            x_new = limit(x_new)
            x.append(x_new)
            v.append(v_new)
            f.append(function(x_new))
            p.append(P[epoch][s] if function(P[epoch][s]) > function(x_new) else x_new)
        # update for one EPOCH
        X.append(x)
        V.append(v)
        F.append(f)
        P.append(p)
        # find the maximum of P[-1]
        score = list(map(function,P[-1]))
        P_BEST.append(P[-1][score.index(max(score))])

    # output & draw
    choice = [0,5,25,50,100,500,1000,2500,5000]
    for i in range(len(choice)):
        plt.subplot(3,3,i+1)
        draw(X,choice[i])
    # plt.tight_layout()
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.2, hspace=0.4)
    
    draw_3D()
    P_FINAL = P_BEST[-1]
    print(P_FINAL)
    print(function(P_FINAL))

    plt.show()