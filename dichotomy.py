def f(x):
    return x**2+6*x+13

def main():
    a = -6
    b = 4
    k = 0
    eps = 0.2
    y = (a + b - eps) / 2
    z = (a + b + eps)/2
    print(f'Промежуток: [{a},{b}]')
    while (abs(b - a) > 2 * eps):
        print('Сравниваем f(yk) с f(zk)')
        if (f(y) <= f(z)):
            print('f(yk) <= f(zk)')
            print(f'Таким образом, a{k+1} = a{k} = {a}; b{k+1} = z{k} = {z}')
            b = z
        else:
            print('f(yk) >= f(zk)')
            print(f'Таким образом, a{k + 1} = y{k} = {y}; b{k + 1} = b{k} = {b}')
            a = y
        print(f'Промежуток:[{a},{b}]')
        y = (a + b - eps) / 2
        z = (a + b +eps)/2
        k += 1
    print(f'x* = {(a + b) / 2} +(-) {(b-a)/2}')
main()
