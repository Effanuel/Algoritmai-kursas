import numpy as np


def quicksort(x):
      if len(x) < 2:
          return x
      else:
          pivot = x[0]
          less = [i for i in x[1:] if i <= pivot]
          greater = [i for i in x[1:] if i > pivot]
          return quicksort(less) + [pivot] + quicksort(greater)
        
def main():
    array = np.random.randint(1, 1000, size=100)
    
    print(quicksort(array))


if __name__ == "__main__":
    main()
