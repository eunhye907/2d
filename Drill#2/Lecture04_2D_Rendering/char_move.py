from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while(True):
    
    x = 0
    while(x<799):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, 90)
        x = x +2
        delay(0.01)


    y = 90
    while(x>799 and y<500):
        clear_canvas_now()
        grass.draw_now(400,30) 
        character.draw_now(800, y)
        y = y +2
        delay(0.01)

    x = 800
    while(x>0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, 500)
        x = x - 2
        delay(0.01)
    
    y=500
    while(y>40):
        clear_canvas_now()
        grass.draw_now(400,30) 
        character.draw_now(1, y)
        y = y - 2
        delay(0.01)

   
close_canvas()

