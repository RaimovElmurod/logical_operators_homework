def main(a,b,c):
    return a<b and b<c or a>b and b>c
print(main(3,4,5))
print(main(6,4,5))
print(main(6,4,1))