spaces = 0


def print_indent(string):
    print("| " * spaces + string)


def fib(n):
    global spaces
    spaces += 1

    if n < 2:
        fibn = n
        print_indent(f"Base case")
        spaces -= 1
        print_indent(f"fib({n}) is {fibn}")
        return fibn

    print_indent(f"Step 1: Find fib({n - 1})")
    fibnm1 = fib(n - 1)

    print_indent(f"Step 2: Find fib({n - 2})")
    fibnm2 = fib(n - 2)

    print_indent(f"Step 3: Add them")
    fibn = fibnm1 + fibnm2
    spaces += 1
    print_indent(f"The sum is {fibn}")

    spaces -= 2
    print_indent(f"fib({n}) is {fibn}")

    return fibn


print("Goal: Find fib(6)")
result = fib(6)
print(f"Done: It is {result}")
