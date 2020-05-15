# defined for n > 0
fib_vals = [0,1]
def fibonacci(n):
    if n < len(fib_vals):
        return fib_vals[n]
    for i in range(len(fib_vals),n+1):
        fib_vals.append(fib_vals[i-1]+fib_vals[i-2])
    return fib_vals[n]

n = 10
for i in range(0,n+1):
    print(fibonacci(i))