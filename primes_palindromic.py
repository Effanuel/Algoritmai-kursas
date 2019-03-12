
def primes(n):
    arr = []
    for i in range(2, n+1):
        ifPrime = True
        for j in range(2, int(i**0.5)+ 1):

            if i % j == 0:
                ifPrime = False
                break
        if ifPrime:
            arr.append(i)

    return arr

def main():

    arr = [int(x) for x in primes(1000) if str(x) == str(x)[::-1]]
    print(arr)


if __name__ == "__main__":
    main()