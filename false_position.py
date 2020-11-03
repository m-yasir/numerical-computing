secantRoot = lambda x0, x1, f: x1-(f(x1)*(x0-x1))/(f(x0)-f(x1))

getApproxError = lambda x_i, x_i_1: abs(x_i_1-x_i)/x_i_1

formatResult = lambda xl, xu, errors, intervals, iters: ((xl, xu), errors, intervals, iters)

def _falseposition(xl, xu, f, currError = 1, calls = None, iters = 1, errors = [], intervals = []) -> (tuple, list, list, int):
    '''
        A standard implementation of self thought out (with no optimization in mind) false position iterative method
        which uses secant method's root finding techinque to calculate next interval's border in a style that is similar to bisection method.
    '''
    if (calls != None and calls <= 0): return formatResult(xl, xu, errors, intervals, iters)
    xr = secantRoot(xl, xu, f)

    if (currError <= 0.01 and prevError < currError): # Change fixed error
        return formatResult(xl, xu, errors, intervals, iters)
    intervals.append((xl, xu))
    print("CURRENT INTERVAL: ", (xl, xu), '\n')
    R = f(xl)*f(xu)
    print("XR: ", xr)
    if R < 0:
        currError = getApproxError(xu, xr)
        errors.append(currError)
        print(f"#{iters} Current Error: ", currError)
        return _falseposition(xl, xr, f, currError, calls and calls - 1, iters + 1)
    elif R > 0:
        currError = getApproxError(xl, xr)
        errors.append(currError)
        print(f"#{iters} Current Error: ", currError)
        return _falseposition(xr, xu, f, currError, calls and calls - 1, iters + 1)
    else:
        print(f"#{iters} Current Error: ", currError)
        return formatResult(xl, xu, errors, intervals, iters)

def falsePosition(xl, xu, f, calls = None):
    '''
        Uses false position iteration bracketing method and returns best interval
    '''
    _, errors, intervals, it = _falseposition(xl, xu, f, 1, calls)
    idx = errors.index(min(errors))
    print()
    print('*'*10 + ' Final Result ' + '*'*10)
    print(f'Best Error: {errors[idx]*100:.2f}%')
    (xl, xu) = intervals[idx]
    print(f'and its Interval: ({xl:.3f},{xu:.3f}) on iteration: {idx+1}/{it-1}')
    return intervals[idx]

fx = lambda x: ( 5*(x**3) ) - ( 5*(x**2) ) + (6*x) - 2
# fx = lambda x: -0.5*(x**2) + 2.5*x + 4.5

falsePosition(0, 1, fx, 4)
    