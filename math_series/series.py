def fibonacci(n):
    value=0
    if n == 0:
        value=0
    if n == 1:
        value=1
    if n > 1:
        value=fibonacci(n-1)+fibonacci(n-2)
    return value

def lucas(n):
    value=0
    if n == 0:
        value = 2
    if n == 1:
        value =3
    if n > 1:
        value=lucas(n-1)+lucas(n-2)
    return value

def sum_series(n,first=0,second=1):
    value=0
    if n == 0:
        value = first
    if n == 1:
        value = first + second
    if n > 1:
        value=sum_series(n-1,first,second)+sum_series(n-2,first,second)
    return value