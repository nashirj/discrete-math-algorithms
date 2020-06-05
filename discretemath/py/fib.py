fib_doc = 'docs/fib_doc.png'


# defined for n > 0
def fibonacci_recursive(n):
    if n < 3:
        return n
    return fib[n-1] + fib[n-2]

# defined for n > 0
fib_vals = [0,1]
def fibonacci_dp(n):
    if n < len(fib_vals):
        return fib_vals[n]
    for i in range(len(fib_vals),n+1):
        fib_vals.append(fib_vals[i-1]+fib_vals[i-2])
    return fib_vals[n]

def main():
    n = 10
    for i in range(0,n+1):
        print(fibonacci_dp(i))

if __name__ == '__main__':
    main()