"""11. 최대공약수를 구하는 함수를 구현하시오"""

def gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a
