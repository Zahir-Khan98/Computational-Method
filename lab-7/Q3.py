def nth_root(n, a, eps):

    #exceptional case handle for 'a'
    if a<0:
        try:
            raise Exception('cannot find the', n,'-th root of', a ,'as', a ,'is negative')
        except Exception as excpt:
            print(excpt)
        exit()

    #n-th root of 'a' if a=0 or 1
    if a == 0:
        return 0.0
    if a == 1:
        return 1.0
    
    #we can define this problem as bisection method. suppose x is a real no. st x^n=a then 'x' is n-th root of a
    # hence in this bisection method problem , function is f(x)=x^n-a and search interval is [0,B], B=max{1,a}


    # defining the search interval [A,B]
    A = 0.0
    B = max(1.0, a)  #as, when a is <1 then B=1 and when a>1 then B=a

    # bisection method root searching loop
    while B - A > eps:
        x = (A + B) / 2
        if x ** n < a:
            A = x
        else:
            B = x

    return f'The {n}-th root of {a} with {eps} tolerance is {x}'
answer=nth_root(n=2,a=5,eps=0.01)
print(answer)