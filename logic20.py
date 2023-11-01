def main(n):
    x1 = n%10
    n//=10
    x2 = n%10
    n//=10
    x3 = n%10
    n//=10
    x4 = n%10
    n//=10
    x5 = n%10
    ones = (x1+ x2 + x3 + x4 + x5)
    zeros = 5 - ones
    return ones> zeros
print(main(1100))
print(main(10011))