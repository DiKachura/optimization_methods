from math import *
eps1 = 0.1
eps2 = 0.15
eps3 = 0.001
M = 10
x01 = 1.5
x02 = 1.5


def F(x1, x2):
    return x1**2 + 8 * x2**2 - x1 * x2 + x1
    #return 2 * x1 ** 2 + x1 * x2 + x2 ** 2


def dFx1x1(x1, x2):
    return (F(x1 + 2 * eps3, x2) - F(x1 + eps3, x2) - F(x1 + eps3, x2) + F(x1, x2)) / (eps3 * eps3)


def dFx1x2(x1, x2):
    return (F(x1 + eps3, x2 + eps3) - F(x1 + eps3, x2) - F(x1, x2 + eps3) + F(x1, x2)) / (eps3 * eps3)


def dFx2x2(x1, x2):
    return (F(x1, x2 + 2 * eps3) - F(x1, x2 + eps3) - F(x1, x2 + eps3) + F(x1, x2)) / (eps3 * eps3)


def gradFx1(x1, x2):
    return (F(x1 + eps3, x2) - F(x1 - eps3, x2)) / (2 * eps3)


def gradFx2(x1, x2):
    return (F(x1, x2 + eps3) - F(x1, x2 - eps3)) / (2 * eps3)


def norma(a, b):
    return sqrt(a * a + b * b)


def det(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def to_invers_matr(matr):
    tmp = matr[0][0]
    deter = abs(det(matr))
    matr[0][0] = matr[1][1] / deter
    matr[1][1] = tmp / deter
    matr[0][1] = -(matr[0][1]) / deter
    matr[1][0] = -(matr[1][0]) / deter


def is_positive_define_matr(a):
    return a[1][1] > 0 and det(a) > 0


def mult_matr_on_vector(a, a1, a2):
    global d1, d2
    d1 = -(a[0][0] * a1 + a[0][1] * a2)
    d2 = -(a[1][0] * a1 + a[1][1] * a2)

def swann_method(f, x0, t):
    flag = True
    a = 0
    b = 0
    k = 0
    x1 = f(x0-t)
    x2 = f(x0)
    x3 = f(x0 + t)
    if (x1>=x2) and (x2<=x3):
        a = x0 - t
        b = x0 + t
        flag = False
    elif (x1<x2) and (x2>x3) or a!=0 and b!=0:
        flag = False
    if (x1>=x2) and (x2>x3):
        delta = t
        a = x0
    else:
        delta = -t
        b = x0
    while flag:
        k+=1
        x_prev = x0
        x0 += pow(2, k-1) * delta
        if (f(x0)<f(x_prev)):
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
        if (fy <= fz):
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
def main():
    global x01, x02
    t = 0
    xk_next1 = x01
    xk_next2 = x02
    xk1 = x01
    xk2 = x02
    k = 0
    flag = 0
    while True:
        print("ИТЕРАЦИЯ " + str(k) + ":")
        print("=======================")
        print("=======================")
        grad1 = gradFx1(xk1, xk2)
        grad2 = gradFx2(xk1, xk2)
        print("grad f(x01) = ", grad1)
        print("grad f(x02) = ", grad2)
        norma_grad_k = norma(grad1, grad2)
        print("||gradf(x)|| = ", norma_grad_k)
        if norma_grad_k < eps1:
            print("Так как ||gradf(x)|| <= " + str(eps1) + ", то вычисления окончены ")
            break
        else:
            print("Так как ||gradf(x)|| > " + str(eps1) + " продолжим вычисления ")
        if k >= M:
            print("Так как k>=M, то вычисления окончены")
            break
        else:
            print("Так как k<M, то продолжим вычисления")
        print("x(k) = (" + str(xk1) + "; " + str(xk2) + ")")
        a = [[dFx1x1(x01, x02), dFx1x2(x01, x02)], [dFx1x2(x01, x02), dFx2x2(x01, x02)]]
        print("Матрица H = ")
        print(a[0][0], a[0][1])
        print(a[1][0], a[1][1])
        print("det = ", det(a))
        to_invers_matr(a)
        if is_positive_define_matr(a):
            mult_matr_on_vector(a, grad1, grad2)
            print("Матрица положительно определена")
            t = 1
        else:
            print("Матрица отрицательно определена")
            break
        print("d=(" + str(d1) + "; " + str(d2) + ")")
        print("t = ", t)
        xk_next1 = xk1 + t * d1
        xk_next2 = xk2 + t * d2
        print("x(k+1) = (" + str(xk_next1) + "; " + str(xk_next2) + ")")

        def f(alpha):
            x_new = [xk1 + alpha * d1, xk2 + alpha * d2]
            return F(x_new[0], x_new[1])

        a, b = swann_method(f, -1, 1)
        print(f'a = {a}, b = {b}')
        tk = the_golden_ratio(f, a, b, eps3)
        print(f'tk = {tk}')
        xk_next1 = xk1 + tk * d1
        xk_next2 = xk2 + tk * d2

        if norma(xk_next1 - xk1, xk_next2 - xk2) < eps2 and abs(F(xk_next1, xk_next2) - F(xk1, xk2)) < eps2:
            print("||x(k+1)-x(k)|| = ", norma(xk_next1 - xk1, xk_next2 - xk2))
            print("|F(x(k+1))-F(x(k))| = ", abs(F(xk_next1, xk_next2) - F(xk1, xk2)))
            flag += 1
        else:
            flag = 0
        if F(xk_next1, xk_next2) > F(xk1, xk2):
            print("F(x(k+1))>F(x(k)) => функция начала возрастать => расчет окончен")
            xk_next1 = xk1
            xk_next2 = xk2
            break
        k += 1
        xk1 = xk_next1
        xk2 = xk_next2
        print("Количество раз, когда ||x(k+1)-x(k)||<= eps2 и |F(x(k+1))-F(x(k))|<=eps2: ", flag)
        if flag == 2:
            print("Поскольку 2 раза подряд ||x(k+1)-x(k)||<= eps2 и |F(x(k+1))-F(x(k))|<=eps2, то расчет окончен")
            break
    print("Минимум функции f(x) =", F(xk_next1, xk_next2))
    print("Точка минимума: x1 =", xk_next1, ", x2 =", xk_next2)


if __name__ == '__main__':
    main()