from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND_FULL.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

frame = 0
direct = 1
x, y = 300, 400
arrow_x, arrow_y = random.randint(0, TUK_WIDTH // 2), random.randint(0, TUK_HEIGHT // 2)
speed = 2

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

def move_character(p1, p2):
    global x, y, direct, frame

    x1, y1 = p1
    x2, y2 = p2

    for i in range(0, 100, 1):
        t = i / 100
        x = (1 - t) * x1 + t * x2
        y = (1 - t) * y1 + t * y2

        if x2 > x1:
            direct = 1
        else:
            direct = 0

        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2 , TUK_HEIGHT // 2)
        arrow.draw(arrow_x, arrow_y)
        character.clip_draw(frame * 100, direct * 100, 100, 100, x, y)
        frame = (frame + 1) % 8

        update_canvas()
        delay(0.01)

running = True
hide_cursor()

while running:

    handle_events()
    move_character((x, y), (arrow_x, arrow_y))
    x, y = arrow_x, arrow_y
    arrow_x, arrow_y = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)

close_canvas()
