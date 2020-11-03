def bisectionMethod(xl, xu, f, currError = 1, calls = None, iters = 1):
    if (calls != None and calls <= 0): return (xl, xu)
    xr = (xl+xu)/2
    
    if (currError <= 0.1):
        return (xl, xu)
    
    R = f(xl)*f(xu)
    if R < 0:
        currError = abs(xr-xu)/xr
        print(f"#{iters} Current Error: ", currError)
        return bisectionMethod(xl, xr, f, currError, calls and calls - 1, iters + 1)
    elif R > 0:
        currError = abs(xr-xl)/xr
        print(f"#{iters} Current Error: ", currError)
        return bisectionMethod(xr, xu, f, currError, calls and calls - 1, iters + 1)
    else:
        print(f"#{iters} Current Error: ", currError)
        return (xl, xu)

# fx = lambda x: ( 5*(x**3) ) - ( 5*(x**2) ) + (6*x) -2
fx = lambda x: -0.5*(x**2) + 2.5*x + 4.5

# print("RESULT: ", bisectionMethod(0, 1, fx))
print("RESULT: ", bisectionMethod(5, 10, fx, 1, 3))
    