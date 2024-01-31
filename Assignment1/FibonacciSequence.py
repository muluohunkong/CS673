def FibonacciSequence(n):
    FibonacciSequence = [1, 1]
    for i in range(2, n):
        FibonacciSequence.append(FibonacciSequence[i-1] + FibonacciSequence[i-2])
    return FibonacciSequence

Result = FibonacciSequence(100)

print(Result)

