from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(1280, 1024)

kpu = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')


def reach_point(x, y, px, py):
    if (x > px - 5) and (x < px + 5) and (y > py - 5) and (y < py + 5):
        return True

def draw_line_perfect(i,p0,p1,p2,p3):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p0[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p2[0] + (t ** 3 - t ** 2) * p3[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p0[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p2[1] + (t ** 3 - t ** 2) * p3[1]) / 2
        return x, y

def goal_current_to_point(point_count):

    global p
    global cx
    global cy
    i = 0
    frame = 0
    dir = 0

    while True:
        clear_canvas_now()
        kpu.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

        px, _ = draw_line_perfect(i, p[point_count % 10], p[(point_count+1) % 10],p[point_count+2 % 10],p[point_count+3 % 10])
        i += 2
        cx, cy = draw_line_perfect(i, p[point_count % 10], p[(point_count+1) % 10],p[point_count+2 % 10],p[point_count+3 % 10])

        if cx - px > 0:
            direction = 1
        else:
            direction = -1

        if direction > 0:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, cx, cy)
        elif direction < 0:
            character.clip_draw(frame * 100, 100 * 0, 100, 100, cx, cy)

        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)

        if i == 100:
            break

def run_character():
    count = 0
    while True:
        goal_current_to_point(count)
        count = (count + 1) % 10


cx, cy = 800 // 2, 90
p = [(random.randint(0 + 50, KPU_WIDTH - 50), random.randint(0 + 50, KPU_HEIGHT - 50)) for i in range(10)]

while True:
    run_character()

close_canvas()