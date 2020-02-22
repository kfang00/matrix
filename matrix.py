"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    x = str()
    y = str()
    z = str()
    one = str()
    for li in matrix:
        x += str(li[0]) + " "
        y += str(li[1]) + " "
        z += str(li[2]) + " "
        one += str(li[3]) + " "
    print(x)
    print(y)
    print(z)
    print(one)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    a = 0
    while a < len(matrix):
        b = 0
        while b < len(matrix):
            if (a == b):
                matrix[a][b] = 1
            else:
                matrix[a][b] = 0
            b += 1
        a += 1



#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    copy = new_matrix(len(m2[0]), len(m2))
    e = 0
    while e < len(m2):
        a = 0
        while a < len(m1[0]):
            sum = 0
            b = 0
            while b < len(m1):
                sum += m1[b][a] * m2[e][b]
                b += 1
            copy[e][a] = sum
            a += 1
        e += 1
    c = 0
    while c < len(m2):
        d = 0
        while d < len(m2[0]):
            m2[c][d] = copy[c][d]
            d += 1
        c += 1

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
