from math import sqrt

def f(x):
    return x**2+6*x+13

def main():
    print('Метод золотого сечения')
    a = -6
    b = 4
    eps = 0.5
    k = 0
    phi = (3 - sqrt(5)) / 2  # константа золотого сечения
    y = a + phi * (b - a)
    z = a + b - y
    fy = f(y)
    fz = f(z)
    print(f'Промежуток: [{a},{b}]\n')
    l = 2 * eps
    while(abs(b-a)>l):
        print('Сравниваем f(yk) с f(zk)')
        print(f'f(y{k}) = {fy}, f(z{k}) = {fz} =>')
        if fy <= fz:

            print(f'f(y{k}) <= f(z{k})')
            print(f'Таким образом, a{k + 1} = a{k} = {a}; b{k + 1} = z{k} = {z}; y{k+1} = a{k+1} + b{k+1} - y{k} = {a+b-y}; z{k+1} = y{k} = {y}')
            b = z

            ind = True
        else:
            print('f(y{k}) > f(z{k})')
            print(f'Таким образом, a{k + 1} = y{k} = {y}; b{k + 1} = b{k} = {b}; y{k+1} = z{k} = {z}; z{k+1} = a{k+1} + b{k+1} - z{k} = {a+b-y}')
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
        print(f'Промежуток:[{a},{b}]\n')
        k += 1
    print(f'x* = {(a + b) / 2} +(-) {(b - a) / 2}')
main()
