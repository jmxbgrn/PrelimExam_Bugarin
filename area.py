import math

class square():
    length = int(input('Length of the square:'))
    width = int(input('Width of the square:'))
    height = int(input('Height of the square:'))

    Area = (length * width * height)
    perimeter = 2 * (length + width)

    print('Area:',Area)
    print('Perimeter:', perimeter)
    
    