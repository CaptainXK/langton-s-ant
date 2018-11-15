import os
from draw_map import *

X=201
Y=201

def _move_(tk, canvas, label, _map, _cur, step):
    if _map.get_color(_cur) == WHITE:
        _map.switch_color(_cur)
        do_draw_map(tk, canvas, label, _map, _cur.x, _cur.y, step)
        _cur._do_move_(RIGHT)
    else:
        _map.switch_color(_cur)
        do_draw_map(tk, canvas, label, _map, _cur.x, _cur.y, step)
        _cur._do_move_(LEFT)

def clear():
    os.system('cls')

def _main_():
    idx = 0
    cur_pos = Pos()
    cur_map = Area(X, Y)

    tk = Tk()
    canvas = Canvas(tk, width = 5 * X, height = 5 * X)
    label = Label(tk, fg='green')
    init_draw(tk, canvas, label, X, Y)

    cur_pos.set_pos( int(X/2), int(Y/2) )

    # cur_map.show()

    while idx < 13000:
        # print("%dth move:"%(idx+1))
        _move_(tk, canvas, label, cur_map, cur_pos, idx+1)
        idx += 1
        # cur_map.show()
        # clear()

    do_end_draw(tk)

_main_()