def mySqrt(x: int) -> int:
    for i in range(0, x+1):
        if i * i == x:
            return i
        elif i * i > x:
            return i-1