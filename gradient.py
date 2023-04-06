import numpy as np
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
    return np.array([derivative_x1(x, eps=1e-10),derivative_x2(x, eps=1e-10)])

def next_x(x, t):
    temp = grad_f(x)
    return x[0] - t*temp[0], x[1] - t*temp[1]

def gradient(x, eps1, eps2, M):
    grad = grad_f(x)
    eps = 1e-15
    t = 0.5
    k = 0

    resolved = False
    while k < M and not resolved:
        k += 1
        if eps1 > np.linalg.norm(grad):
            print(f'если || grad(fx{k})|| < eps1, т.е. {np.linalg.norm(grad)} < {eps1}')
            resolved = True
        else:
            print(f'если || grad(fx{k})|| >= eps1, т.е. {np.linalg.norm(grad)} >= {eps1}')
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
            print(f'x1 = {x[0]}, x2 = {x[1]},\nf(x) =  {differentiable_function(x[0], x[1])}')

gradient([1.5, 0.1], 0.1, 0.15, 10)