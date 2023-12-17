import time
epsilon = 1e-15

def midpoint(upper, lower, n):
    summation = 0
    hight = 0
    d = (upper - lower) / n
    for i in range(n):
        hight = (1 / (lower + ((i*2+1)*d)/2))
        summation += hight
    summation *= d
    return summation

def compute_using_integral():
    """
    用積分定義跟 midpoint 來算 e
    停止標準是到小數點後第4位 不然用 python 太慢了
    """
    start = time.process_time()
    e = 1
    while True:
        #print(e)
        tmp = abs(midpoint(e, 1, 100) - 1)
        if tmp < 0.00001: break
        e += 0.00001
    end = time.process_time()

    return e, (end-start)

def compute_using_limit():
    """
    用極限的定義來求 e
    停止的條件是如果加上去的值小於 epsilon 的時候
    """
    start = time.process_time()
    n = 1
    e = (1 + 1 / n) ** n
    while True:
        n += 1
        next_e = (1 + 1 / n) ** n
        if abs(next_e - e) < epsilon:
            break
        e = next_e
    end = time.process_time()
    return e, (end-start)

def compute_using_summation():
    """
    用 summation 來求 e
    停止的條件是如果加上去的值小於 epsilon 的時候
    """
    start = time.process_time()
    e = 1
    n = 1
    factorial = 1
    while True:
        factorial *= n
        term = 1 / factorial
        if term < epsilon:
            break
        e += term
        n += 1
    end = time.process_time()
    return e, (end-start)

e_integral, time_integral = compute_using_integral()
e_limit, time_limit = compute_using_limit()
e_summation, time_summation = compute_using_summation()

print("Compute using :")
print("Integral  : %.15f - Time : %.10f"%(e_integral, time_integral))
print("Limit     : %.15f - Time : %.10f"%(e_limit, time_limit))
print("Summation : %.15f - Time : %.10f"%(e_summation, time_summation))
