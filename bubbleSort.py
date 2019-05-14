import timeit
import numpy as np


def bubbleSort(arr):
    if len(arr) == 1:
        return arr
    else:
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i+1], arr[i] = arr[i], arr[i+1]
        return [arr[-1]] + bubbleSort(arr[:-1])


def test():
    arr = list(np.random.randint(1, 1000, 10)) #over 800 exceeds recursion limit
    print(arr)
    print(bubbleSort(arr))

def main():

    start_time = timeit.default_timer()
    test()
    print(timeit.default_timer() - start_time)


if __name__ == '__main__':
    main()
