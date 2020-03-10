import pyglet
import sys
import requests
from datetime import datetime

from weather import Weather
from transit import Transit

class UI(pyglet.window.Window):
  def __init__(self, *args, **kwargs):
    super(UI, self).__init__(*args, **kwargs)
    pink = (250, 132, 246, 255)
    self.bg    = pyglet.image.SolidColorImagePattern(pink).create_image(self.width, self.height)
    y_val = self.height - self.height // 4
    self.time = pyglet.text.Label('', font_name='Avenir', font_size=48, x=self.width//2, y=y_val, anchor_x="center", anchor_y="center")
    self.date = pyglet.text.Label('', font_name='Avenir', font_size=24, x=self.width//2, y = y_val - 50, anchor_x="center", anchor_y="center")

  def on_key_press(self, symbol, modifiers):
    sys.exit(0)

  def draw_time(self):
    now = datetime.now()

    time_text = now.strftime("%I:%M%p")
    if time_text[0] == '0':
      time_text = time_text[1:]

    self.time.text = time_text
    self.time.draw()

    date_text = now.strftime("%A, %B %d, %Y")
    self.date.text = date_text
    self.date.draw()


  def on_draw(self):
    self.clear()
    self.bg.blit(0, 0)
    self.draw_time()

class Box:
  pass


if __name__ == '__main__':
  w = Weather()
  ui = UI(fullscreen=True)
  #t = Transit()
  pyglet.app.run()
