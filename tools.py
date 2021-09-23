from PIL import Image, ImageDraw
from tubes import tubesOriginal

"""
Color:

1 - red
2 - green
3 - blue
4 - yellow
5 - pink
6 - grey
7 - light blue
8 - purple
9 - orange
10 - brown
11 - dark green
12 - lime

"""
colors = {
    "0": (255,255,255),
    "1": (255,0,0),
    "2": (0,255,0),
    "3": (0,0,255),
    "4": (255,247,0),
    "5": (245, 2, 204),
    "6": (135, 135, 135),
    "7": (7, 240, 232),
    "8": (170, 12, 237),
    "9": (237, 162, 12),
    "10": (87, 58, 0),
    "11": (5, 92, 0),
    "12": (147, 201, 103),

}

class Bubble:
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color

    def draw(self, draw:ImageDraw):
        draw.ellipse((self.x, self.y, self.x+self.r, self.y+self.r), fill=self.color, outline=(0,0,0))


def visualizeTubes():

    im = Image.new('RGB', (500,300), (255, 255, 255))
    draw = ImageDraw.Draw(im)

    b_r = 20
    cols = round(len(tubesOriginal)/2)

    bubbles = []

    x = 50
    y = 30
    i = 1
    for tube in tubesOriginal:
        j = 0
        for b in tube:
            bubbles.append(Bubble(x,y,b_r,colors[str(b)]))
            y += b_r+1
            j += 1
        x += 50
        i += 1
        y = 30
        if i > cols:
            if i == (cols+1):
                x = 50
            y = 170
        

    for b in bubbles:
        b.draw(draw)

    im.save('tubes.jpg', quality=95)


visualizeTubes()

