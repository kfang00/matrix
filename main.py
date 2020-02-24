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
clothes = []
add_edge(clothes, 120, 300, 0, 150, 300, 0)
add_edge(clothes, 150, 340, 0, 120, 340, 0)
add_edge(clothes, 120, 400, 0, 180, 400, 0)
add_edge(clothes, 180, 440, 0, 250, 440, 0)
add_edge(clothes, 250, 400, 0, 250, 440, 0)
add_edge(clothes, 320, 440, 0, 320, 400, 0)
add_edge(clothes, 180, 400, 0, 380, 400, 0)
add_edge(clothes, 380, 340, 0, 350, 340, 0)
add_edge(clothes, 350, 300, 0, 380, 300, 0)
hair= []
add_edge(hair, 250, 50, 0, 250, 20, 0)
add_edge(hair, 250, 50, 0, 235, 25, 0)
add_edge(hair, 250, 50, 0, 265, 25, 0)
feet = []
add_edge(feet, 180, 440, 0, 150, 440, 0)
add_edge(feet, 150, 470, 0, 250, 470, 0)
add_edge(feet, 250, 440, 0, 250, 470, 0)
add_edge(feet, 350, 470, 0, 350, 440, 0)
eye1 = []
add_edge(eye1, 175, 125, 0, 225, 125, 0)
add_edge(eye1, 225, 175, 0, 175, 175, 0)
eye2 = []
add_edge(eye2, 275, 125, 0, 325, 125, 0)
add_edge(eye2, 325, 175, 0, 275, 175, 0)

draw_lines( body, screen, color )
draw_lines( feet, screen, color )
color = [ 175, 178, 182 ]
draw_lines( glasses, screen, color )
color = [ 0, 111, 255 ]
draw_lines( clothes, screen, color )
color = [ 255, 255, 255 ]
draw_lines( hair, screen, color )
draw_lines( eye1, screen, color )
draw_lines( eye2, screen, color )
display(screen)
save_ppm(screen, 'binary.ppm')
save_ppm_ascii(screen, 'ascii.ppm')
save_extension(screen, 'img.png')
