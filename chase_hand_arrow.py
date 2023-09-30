from pico2d import *

open_canvas()

tuk_ground = load_image('TUK_GROUND.png')
character = load_image('blueHeadCharacter.png')
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
running = True
anim = 0
x = 800 // 2
y = 600 // 2

def handle_events():
    global running, anim, x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                anim = 1
            elif event.key == SDLK_LEFT:
                anim = 2
            elif event.key == SDLK_UP:
                anim = 3
            elif event.key == SDLK_DOWN:
                anim = 4
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            anim = 0
frame = 0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if anim == 0:
        character.clip_draw(114, 560 - frame * 114, 114, 114, x, y)
    elif anim == 1:
        character.clip_draw(frame * 114 + 684, 560, 114, 114, x, y)
        x += 5
    elif anim == 2:
        character.clip_composite_draw(frame * 114 + 684, 560, 114, 114, 0, 'h',  x, y, 114, 114)
        x -= 5
    elif anim == 3:
        character.clip_draw(0 + frame * 115, 0, 114, 113, x, y)
        y += 5
    elif anim == 4:
        character.clip_draw(0 + frame * 115, 0, 114, 113, x, y)
        y -= 5
    update_canvas()
    handle_events()
    frame = (frame + 1) % 3
    delay(0.05)
