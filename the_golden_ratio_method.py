from math import sqrt


def f(x):
    return x**2+6*x+13

# Метод золотого сечения
#def Golden_ratio(f, a, b, eps):
def main():
    print('Метод золотого сечения')
    a = -6
    b = 4
    eps = 0.5
    k = 0
    phi = (3 - sqrt(5)) / 2  # константа золотого сечения
    y = a+phi*(b-a)
    z = a+b-y
    print(f'Промежуток: [{a},{b}]\n')
    while(abs(b-a)>2*eps):
        print('Сравниваем f(yk) с f(zk)')
        print(f'f(y{k}) = {f(y)}, f(z{k}) = {f(z)} =>')
        if f(y) <= f(z):
            y0 = y
            print(f'f(y{k}) <= f(z{k})')
            print(f'Таким образом, a{k + 1} = a{k} = {a}; b{k + 1} = z{k} = {z}; y{k+1} = a{k+1} + b{k+1} - y{k} = {a+b-y0}; z{k+1} = y{k} = {y0}')
            b=z
            y=a+b-y0
            z=y0
        else:
            print('f(y{k}) > f(z{k})')
            print(f'Таким образом, a{k + 1} = y{k} = {y}; b{k + 1} = b{k} = {b}; y{k+1} = z{k} = {z}; z{k+1} = a{k+1} + b{k+1} - z{k} = {a+b-y}')
            a=y
            y=z
            z=a+b-y
        print(f'Промежуток:[{a},{b}]\n')
        k+=1
    print(f'x* = {(a + b) / 2} +(-) {(b - a) / 2}')
main()
