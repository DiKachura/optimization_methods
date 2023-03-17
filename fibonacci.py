# Функция f(x)
def f(x):
    return x ** 2 + 6 * x + 13

def fibonacci(f, a, b, eps):
    print('Метод Фибоначчи:')
    l = 2*eps
    fn, fn1, n = 1, 1, 1
    R = abs(b-a)/l
    while fn < R:
        fn, fn1, n = fn + fn1, fn, n + 1
    k = 0
    z = a + fn1 / fn * (b - a)
    y = a + b - z
    fy = f(y)
    fz = f(z)
    print(f'Промежуток: [{a},{b}]\n')
    while k < n - 3:
        print('Сравниваем f(yk) с f(zk)')
        print(f'f(y{k}) = {fy}, f(z{k}) = {fz} =>')
        if fy <= fz:
            print(f'f(y{k}) <= f(z{k})')
            print(f'Таким образом, a{k + 1} = a{k} = {a}; b{k + 1} = z{k} = {z}; y{k + 1} = a{k + 1} + b{k + 1} - y{k} = {a + b - y}; z{k + 1} = y{k} = {y}')
            b = z
            z = y
            fz = fy
            ind = True
        else:
            print('f(y{k}) > f(z{k})')
            print(f'Таким образом, a{k + 1} = y{k} = {y}; b{k + 1} = b{k} = {b}; y{k + 1} = z{k} = {z}; z{k + 1} = a{k + 1} + b{k + 1} - z{k} = {a + b - y}')
            a = y
            y = z
            fy = fz
            ind = False
        if ind == True:
            y = a + b - z
            fy = f(y)
        else:
            z = a + b - y
            fz = f(z)
        print(f'Промежуток:[{a},{b}]\n')
        k += 1
    print(f'k = N - 3 = {n - 3}')
    y = (a+b)/2
    z = y + eps
    fy = f(y)
    fz = f(z)
    if fy <= fz:
        print(f'f(y{n-1}) <= f(z{n-1})')
        print(f'Таким образом: a{n-1} = a{n-2} = {a}; b{n-1} = z{n-1} = {z}')
        b = z
    else:
        print(f'f(y{n - 1}) > f(z{n - 1})')
        print(f'Таким образом: a{n - 1} = y{n - 1} = {y}; b{n - 1} = b{n - 2} = {b}')
        a = y
    print(f'Промежуток:[{a},{b}]\n')
    print(f'x* = {(a + b) / 2} +(-) {(b - a) / 2}')

def main():
    a = -6
    b = 4
    eps = 0.5
    fibonacci(f, a, b, eps)
if __name__ == '__main__':
    main()
