def falsePosition(xl, xu, f, currError = 1, calls = None, iters = 1):
    if (calls != None and calls <= 0): return (xl, xu)
    xr = xu-(f(xu)*(xl-xu))/(f(xl)-f(xu))
    
    # TODO: Stop if error increases
    if (currError <= 0.01): # Change fixed error
        return (xl, xu)
    print("CURRENT INTERVAL: ", (xl, xu), '\n')
    R = f(xl)*f(xu)
    print("XR: ", xr)
    if R < 0:
        currError = abs(xr-xu)/xr
        print(f"#{iters} Current Error: ", currError)
        return falsePosition(xl, xr, f, currError, calls and calls - 1, iters + 1)
    elif R > 0:
        currError = abs(xr-xl)/xr
        print(f"#{iters} Current Error: ", currError)
        return falsePosition(xr, xu, f, currError, calls and calls - 1, iters + 1)
    else:
        print(f"#{iters} Current Error: ", currError)
        return (xl, xu)

fx = lambda x: ( 5*(x**3) ) - ( 5*(x**2) ) + (6*x) -2
# fx = lambda x: -0.5*(x**2) + 2.5*x + 4.5

print("RESULT: ", falsePosition(0, 1, fx, 1, 4))
# print("RESULT: ", falsePosition(5, 10, fx, 1, 3))
    