import math

getApproxError = lambda x_i, x_i_1: abs(x_i_1-x_i)/x_i_1

def fixed_point(x0, f, g, iterations):
    '''
        Implements simple fixed point iteration method as taught in numerical analysis course.
        Probably the simplest iterative numerical method.
        This is iterative on purpose as compared to previous recursive implementations of iterative methods in the repo.
    '''
    current_error = 1
    prev_error = 2
    xn = x0
    print(f'n\t\txn\t\terror')
    print(f'**\t\t****\t\t****')
    for i in range(iterations):
        xr = g(xn)
        prev_error = current_error
        current_error = getApproxError(xn, xr)
        print(f'{i+1}\t\t{xr:.3f}\t\t{current_error*100:.2f}')
        if current_error > prev_error: break
        xn = xr
    return xn

f = lambda x: math.e**(-x)-x
g = lambda x: (x**2+3)/2

print(f'xn: {fixed_point(0, f, g, 5)}')