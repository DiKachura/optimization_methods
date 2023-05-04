"""import numpy as np
from fibonacci import fibonacci
from swann_method import swann_method
'''
f(x) = x1^2 + 8x2^2 - x1x2 + x1
x0 = (1,5; 0,1)
'''
def differentiable_function(x1, x2):
    return x1**2 + 8 * x2**2 - x1 * x2 + x1

def derivative_x2(x, eps):
    return (differentiable_function(x[0], x[1] + eps) - differentiable_function(x[0], x[1])) / eps

def derivative_x1(x, eps):
    return (differentiable_function(x[0] + eps, x[1]) - differentiable_function(x[0], x[1])) / eps

def grad_f(x):
    return np.array([derivative_x1(x, eps=1e-10), derivative_x2(x, eps=1e-10)])

def next_x(x, t):
    temp = grad_f(x)
    return x[0] - t*temp[0], x[1] - t*temp[1]


def ft(x, xk, tk):
    return differentiable_function(x)

def gradient(x, eps1, eps2, M):
    grad = grad_f(x)
    k = 0
    if np.linalg.norm(grad) < eps1:
        print(f'x* = {x}')
    else:
        if k >= M:
            print(f'x* = {x}')
        else:
            t = swann_method(x, 1)
    '''grad = grad_f(x)
    eps = 1e-15
    k = 0
    resolved = False
    a, b = swann_method(x, 1)
    while k < M and not resolved:
        k += 1
        if eps1 > np.linalg.norm(grad):
            print(f'если || grad(fx{k})|| < eps1, т.е. {np.linalg.norm(grad)} < {eps1}')
            resolved = True
        else:
            print(f'если || grad(fx{k})|| >= eps1, т.е. {np.linalg.norm(grad)} >= {eps1}')
            t = fibonacci(differentiable_function(x[0], x[1], ))
            newx, newy = next_x(x, t)
            while not differentiable_function(newx, newy) - differentiable_function(x[0], x[1]) < - eps * np.linalg.norm(grad) ** 2:
                print(f'если f(x{k+1}) - f(x{k}) < -eps * ||grad(f(x{k}))^2, т.е. {differentiable_function(newx, newy) - differentiable_function(x[0], x[1])} < {- eps * np.linalg.norm(grad) ** 2} и')
                x[0], x[1] = newx, newy
                print(f'x{k} = {x[0]}, x{k} = {x[1]}')
                t/=2
                newx, newy = next_x(x, t)
                print(f'x{k+1} = {newx}, x{k+1} = {newy}')
            if np.sqrt((x[0] - newx) ** 2 + (x[1] - newy) ** 2) < eps2 and np.fabs(differentiable_function(newx, newy) - differentiable_function(x[0], x[1])) < eps2:
                print(f'||x{k+1} - x{k}|| < eps2 и |f(x{k+1}) - f(x{k})| < eps2, т.е. {np.sqrt((x[0] - newx) ** 2 + (x[1] - newy) ** 2)} < {eps2} и {np.fabs(differentiable_function(newx, newy) - differentiable_function(x[0], x[1]))} < {eps2}')
                resolved = True
            k+=1
            x[0], x[1] = newx, newy
            print(f'x1 = {x[0]}, x2 = {x[1]},\nf(x) =  {differentiable_function(x[0], x[1])}')'''

gradient([1.5, 0.1], 0.1, 0.15, 10)"""




import numpy as np
from math import *

def differentiable_function(x1, x2):
    #return x1**2 + 8 * x2**2 - x1 * x2 + x1
    return 2*x1**2+x1*x2+x2**2
def derivative_x2(x, eps):
    return (differentiable_function(x[0], x[1] + eps) - differentiable_function(x[0], x[1])) / eps

def derivative_x1(x, eps):
    return (differentiable_function(x[0] + eps, x[1]) - differentiable_function(x[0], x[1])) / eps

def grad_f(x):
    return np.array([derivative_x1(x, eps=1e-10), derivative_x2(x, eps=1e-10)])


def swann_method(f, x0, t):
    flag = True
    a = 0
    b = 0
    k = 0
    x1 = f(x0-t)
    x2 = f(x0)
    x3 = f(x0 + t)
    if (x1>=x2).all() and (x2<=x3).all():
        a = x0 - t
        b = x0 + t
        flag = False
    elif (x1<x2).all() and (x2>x3).all() or a!=0 and b!=0:
        flag = False
    if (x1>=x2).all() and (x2>x3).all():
        delta = t
        a = x0
    else:
        delta = -t
        b = x0
    while flag:
        k+=1
        x_prev = x0
        x0 += pow(2, k-1) * delta
        if (f(x0)<f(x_prev)).all():
            if delta > 0:
                a = x_prev
            else:
                b = x_prev
        else:
            if delta < 0:
                a = x0
            else:
                b = x0
            flag = False
    return a, b

def the_golden_ratio(f, a, b, eps):
    k = 0
    phi = (3 - sqrt(5)) / 2
    y = a + phi * (b - a)
    z = a + b - y
    fy = f(y)
    fz = f(z)
    l = 2 * eps
    while(abs(b-a)>l):
        if (fy <= fz).all():
            b = z
            ind = True
        else:
            a = y
            ind = False
        if ind == True:
            z = y
            fz = fy
            y = a + b - z
            fy = f(y)
        else:
            y = z
            fy = fz
            z = a + b - y
            fz = f(z)
        k += 1
    return (a+b)/2

def gradient_descent(x0, eps, eps1, eps2, M):
    x = x0
    k = 0
    while True:
        print(f'шаг {k}')
        grad = grad_f(x)
        if np.linalg.norm(grad) < eps1:
            print(f'grad < eps1, т.е. {np.linalg.norm(grad)} < {eps1}')
            break
        if k >= M:
            print(f'k >= M, т.е. {k} >= {M}')
            break
        #grad = grad_f(x)
        print(f'grad = {grad}')
        def f(alpha):
            x_new = [x[0] - alpha * grad[0], x[1] - alpha * grad[1]]
            #print(f'x_new = {x_new}')
            return grad_f(x_new)

        a, b = swann_method(f, 0, 1)
        print(f'a = {a}, b = {b}')
        tk = the_golden_ratio(f, a, b, eps)
        print(f'tk = {tk}')
        x_next = x - tk * grad
        print(f'x_next = {x_next}')
        if np.linalg.norm(x_next - x) < eps2 and abs(differentiable_function(x_next[0], x_next[1]) - differentiable_function(x[0], x[1])) < eps2:
            print(f'последняя проверка')
            break
        x = x_next
        print(f'x = {x}')
        k += 1
    return x
x0 = [0.5, 1]
x = gradient_descent(x0, eps=1e-5, eps1=0.1, eps2=0.15, M=10)
print(x)