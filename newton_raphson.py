getApproxError = lambda x_i, x_i_1: abs(x_i_1-x_i)/x_i_1 # For Percent error

def _NR_(xn, f, fp, iterations, n = 1, c_error = 1, p_error = 2):
    if iterations == 0 or c_error > p_error:
        return xn
    
    xr = xn - f(xn)/fp(xn)
    
    
    p_error = c_error
    
    c_error = getApproxError(xn, xr)
    
    print(f'{n}\t{xn:.8f}\t\t{c_error*100}%')
    
    return _NR_(xr, f, fp, iterations - 1, n + 1, c_error, p_error)

def newtonRaphson(x, f, fp, iterations):
    return _NR_(x, f, fp, iterations)

f = lambda x: (x**3)-(2*x**2)-5
fp = lambda x: 3*(x**2)-(4*x)
x0 = 2

print('n\txn\t\t\terror')
print('**\t**********\t\t***************')
newtonRaphson(x0, f, fp, 6)