if __name__ == "__main__":
    N = int(input())
    rest = N % 3
    N //= 3
    if N & 1:
        if rest & 1:
            print("CY")
        else:
            print("SK")
    else:
        if rest & 1:
            print("SK")
        else:
            print("CY")
