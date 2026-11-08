import pyglet
import datetime

window = pyglet.window.Window(400, 200, caption='Pyglet Clock')
label = pyglet.text.Label('Loading...',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

def update_time(dt):
    now = datetime.datetime.now().strftime('%H:%M:%S')
    label.text = now

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.clock.schedule_interval(update_time, 1.0)
pyglet.app.run()
