import timeit
import numpy as np

def selectionSort_v1(arr):
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            # Select the smallest valu
            if arr[j] < arr[minimum]:
                minimum = j

        arr[minimum], arr[i] = arr[i], arr[minimum]
    return arr

def selectionSort_v2(arr):
    if len(arr) == 1:
        return arr
    else:
        max = 1e6
        for i in arr:
            if i < max:
                max = i
        arr.remove(max)
        return [max] + selectionSort_v2(arr)


def test():
    arr = list(np.random.randint(1, 1000, 800)) #over 800 exceeds recursion limit
    #print(arr)
    selectionSort_v2(arr)

def main():

    start_time = timeit.default_timer()
    test()
    print(timeit.default_timer() - start_time)


if __name__ == '__main__':
    main()
