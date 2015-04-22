from operator import pos
from kivy.app import App
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from layout import Layout, Tile


class MyPaintWidget(Widget):
    def __init__(self, **kwargs):
        super(MyPaintWidget, self).__init__(**kwargs)
        self.layout = Layout()
        self.layout.load_from_file("test.lay")
        self.colors = {Tile.Empty: [0.1, 0.1, 0.1],
                       Tile.Wall: [.1, .1, 1],
                       Tile.Start: [1, 1, 0]}

        self.redraw()


    def redraw(self):
        with self.canvas:

            ysize, xsize = self.layout.shape
            for y in range(ysize):
                for x in range(xsize):
                    print x,y
                    Color(rgb=self.colors[self.layout.grid[y][x]])
                    Rectangle(pos=(20 * x, 20 * y), size=(20, 20))

            Rectangle(pos=(20, 200), size=(20, 20))

    def on_touch_down(self, touch):
        with self.canvas:
            Color(1, 1, 0)
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class MyPaintApp(App):
    def build(self):
        return MyPaintWidget()


if __name__ == '__main__':
    MyPaintApp().run()