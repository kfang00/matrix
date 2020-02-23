from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
#m2 = []
#add_edge(m2, 1, 2, 3, 4, 5, 6)
#print_matrix(m2)
#m1 = new_matrix()
#ident(m1)
#print_matrix(m1)
#matrix_mult(m1, m2)
#print_matrix(m2)
#m = []
#add_point(m,1,2,3)
#add_point(m,4,5,6)
#add_point(m,7,8,9)
#add_point(m,10,11,12)
#print_matrix(m)
#matrix_mult(m, m2)
#print_matrix(m2)

matrix = []
add_edge(matrix, 120, 50, 0, 380, 50, 0)
add_edge(matrix, 120, 50, 0, 120, 400, 0)
add_edge(matrix, 380, 50, 0, 380, 400, 0)
add_edge(matrix, 120, 400, 0, 380, 400, 0)

draw_lines( matrix, screen, color )
display(screen)
