import add

def fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a+b

Y = 0
WIDTH = 1
RGB =  [255, 0, 0]

def main():
    global Y, WIDTH, RGB

    full_array = list(fibonacci(45))
    array = full_array[1:]


    _X = 1
    _Y = 0
    add.rectangle3D([0, Y, 0], [1, 1, 1], RGB) #1(,)
    #add.rectangle3D([0, Y, 1], [1, WIDTH, 1], [0, 255, 255]) #1(,)
    for i, el in enumerate(array):
        HEIGHT = el/2

        if i <= 10:
            RGB_ARRAY = [255, 25.5*i, 0]
        elif 10 < i and i <= 20:
            RGB_ARRAY = [255-(25*(i-10)), 255, 0]
            print(RGB_ARRAY, "++ <")
        elif 20 < i and i <= 30:
            RGB_ARRAY = [0, 255, 25.5*(i-20)]
        elif 30 < i and i <= 40:
            RGB_ARRAY = [0, 255-(25.5*(i-30)), 255]
        elif 40 < i and i <= 50:
            RGB_ARRAY = [int(25.5*(i-40)), 0, 255]
        elif 50 < i and i <= 60:
            RGB_ARRAY = [255, 0, 255-(25.5*(i-50))]
        print(RGB_ARRAY, i)

        if i == 0:
            add.rectangle3D([0, Y, 1], [1, HEIGHT, 1], RGB_ARRAY) #1(,)
            continue

        if i % 4 == 1:
            #print(_X, _Y)
            new_Y = _Y + array[i-1]/2 + el/2
            new_X = _X - (el/2 - array[i-1]/2)
            add.rectangle3D([new_Y, Y, new_X], [el, HEIGHT, el], RGB_ARRAY)
            _X = new_X
            _Y = new_Y
            continue
        elif i % 4 == 2:
            new_Y = _Y - (el/2 - array[i-1]/2)
            new_X = _X - el/2 - array[i-1]/2
            add.rectangle3D([new_Y, Y, new_X], [el, HEIGHT, el], RGB_ARRAY)
            _X = new_X
            _Y = new_Y
            continue
        elif i % 4 == 3:
            new_X = _X + el/2 - array[i-1]/2
            new_Y = _Y - el/2 - array[i-1]/2
            add.rectangle3D([new_Y, Y, new_X], [el, HEIGHT, el], RGB_ARRAY)
            _X = new_X
            _Y = new_Y
            continue
        elif i % 4 == 0:
            new_X = _X + el/2 + array[i-1]/2
            new_Y = _Y - array[i-1]/2 + el/2
            add.rectangle3D([new_Y, Y, new_X], [el, HEIGHT, el], RGB_ARRAY)
            _X = new_X
            _Y = new_Y
            continue
    add.off('fibonacci_v4.off')


if __name__ == '__main__':
    main()
