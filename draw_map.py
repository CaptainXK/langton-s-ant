import tkinter
from tkinter import *

WHITE=0
BLACK=1

UP=0
RIGHT=1
DOWN=2
LEFT=3

COLOR = ['white', 'black']
INIT_COL = 0

BASE_X=BASE_Y=4

class Pos:
    x=0
    y=0
    dir=0

    def __init__(self):
        self.x = 0
        self.y = 0
        self.dir = UP

    def set_pos(self, _x, _y):
        self.x = _x
        self.y = _y
        self.dir = UP

    def check_pos_valid(self, _X, _Y):
        if self.x < 0 or self.x >= _X or self.y < 0 or self.y >= _Y:
            return 1
        else:
            return 0
    
    def _do_move_(self, _dir_):
        #towards up
        if self.dir == UP:
            if _dir_ == LEFT:
                self.y -= 1
                self.dir = LEFT
            else:
                self.y += 1
                self.dir = RIGHT
        
        #towards right
        elif self.dir == RIGHT:
            if _dir_ == LEFT:
                self.x -= 1
                self.dir = UP
            else:
                self.x += 1
                self.dir = DOWN

        #towards down
        elif self.dir == DOWN:
            if _dir_ == LEFT:
                self.y += 1
                self.dir = RIGHT
            else:
                self.y -= 1
                self.dir = LEFT

        #towards left
        else:
            if _dir_ == LEFT:
                self.x += 1
                self.dir = DOWN
            else:
                self.x -= 1
                self.dir = UP

class Area:
    _map_=[[]]    

    def __init__(self, X, Y):
        self._map_ = [ [0 for i in range(X)] for i in range(Y)]

    def get_color(self, _cur_pos_):
        return self._map_[_cur_pos_.x][_cur_pos_.y]
    
    def show_color(self, _x, _y):
        return self._map_[_x][_y]

    def switch_color(self, _cur_pos_):
        self._map_[_cur_pos_.x][_cur_pos_.y] = (self._map_[_cur_pos_.x][_cur_pos_.y] + 1) % 2

    def show(self):
        i=0
        j=0
        for i in range(X):
            for j in range(Y):
                print( "%d"%(self.show_color(i,j)), end='') 
                
            print("\n")

def init_draw(tk, canvas, label, X, Y):

    print("Draw %d:%d map"%(X, Y))
    label.config(text=str(0))
    label.pack()#.pack() is used to control the presentation of component
    canvas.pack()

    for i in range(0, X-1, 1):
        for j in range(0, Y-1, 1):
            x_lu = i * 5 + BASE_X
            y_lu = j * 5 + BASE_Y
            canvas.create_rectangle(x_lu, y_lu, x_lu + 5, y_lu + 5, fill='white')

    tk.update()    


def do_draw_map(tk, canvas, label, _map, _x, _y, step):
    label.config(text=str(step) + ' step')

    #define left-up pos
    x_lu = _x * 5 + BASE_X
    y_lu = _y * 5 + BASE_Y
    fill_col = 'red'
    if _map.show_color(_x, _y) == BLACK:
        fill_col = 'black'
    else:
        fill_col = 'white'
    canvas.create_rectangle(x_lu, y_lu, x_lu + 5, y_lu + 5, fill=fill_col)

    #dynamic change pic
    tk.update()

def do_end_draw(tk):
    tk.mainloop()
    

    

