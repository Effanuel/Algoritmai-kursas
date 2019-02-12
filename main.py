import numpy as np
array = np.random.randint(1, 100, size=10000)


def quicksort(x):
      if len(x) < 2:
          return x
      else:
          pivot = x[0]
          less = [i for i in x[1:] if i <= pivot]
          greater = [i for i in x[1:] if i > pivot]
          return quicksort(less) + [pivot] + quicksort(greater)
        


if __name__ == "__main__":
    quicksort(array)