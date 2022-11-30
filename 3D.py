from ursina import *

app = Ursina()

obj = Entity(model='cube', color=color.white)

def update():   # update gets automatically called.
    obj.x += held_keys['d'] * 1
    obj.x -= held_keys['a'] * 1

def update():
    obj.rotation_y+= 30 * time.dt
    obj.rotation_x+= 40 * time.dt
    
app.run()