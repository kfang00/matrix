from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 255, 255, 0 ]
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

body = []
add_edge(body, 120, 50, 0, 380, 50, 0)
add_edge(body, 380, 400, 0, 120, 400, 0)
glasses = []
add_edge(glasses, 120, 150, 0, 140, 150, 0)
add_edge(glasses, 140, 100, 0, 240, 100, 0)
add_edge(glasses, 240, 150, 0, 260, 150, 0)
add_edge(glasses, 260, 100, 0, 360, 100, 0)
add_edge(glasses, 360, 150, 0, 380, 150, 0)
add_edge(glasses, 360, 150, 0, 360, 200, 0)
add_edge(glasses, 260, 200, 0, 260, 150, 0)
add_edge(glasses, 240, 150, 0, 240, 200, 0)
add_edge(glasses, 140, 200, 0, 140, 150, 0)

draw_lines( body, screen, color )
color = [ 255, 255, 255 ]
draw_lines( glasses, screen, color )
display(screen)
save_ppm(screen, 'binary.ppm')
save_ppm_ascii(screen, 'ascii.ppm')
save_extension(screen, 'img.png')
