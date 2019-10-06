from PIL import Image, ImageDraw
import cmath
import math

img = Image.new('RGBA', (1000,1000), color=(0, 0, 0, 0))


def equation(point1, point2):  # Returns components in the form y=mx+c for the straight line between two points.
    m: float = (point1[1]-point2[1])/(point1[0]-point2[0])
    c: float = point1[1] - (m * point1[0])
    return m, c


def rectangle(centre, height, width, angle, colour):
    coords = [(0-width, 0-height),  # Turn width and height into a rectangle
              (0+width, 0-height),
              (0+width, 0+height),
              (0-width, 0+height), ]
    rotation = math.radians(angle)  # Degrees to Radians
    translatedcoords = []
    for point in coords:
        point = complex(point[0], point[1])  # Turns to complex format
        if angle != 0:
            point = cmath.rect(abs(point), cmath.phase(point) + rotation)  # Rotate
        point = (point.real + centre[0], point.imag + centre[1])  # Translate to true centre
        translatedcoords.append(point)
    draw.polygon(translatedcoords, outline=colour)


def circle(centre, radius, colour):
    xTop = centre[0] - radius
    yTop = centre[1] - radius
    xBot = centre[0] + radius
    yBot = centre[1] + radius
    coord = [(xTop, yTop), (xBot, yBot)]
    draw.ellipse(coord, outline=colour)


def line(point1, point2, width, colour):
    draw.line([point1, point2], width=width, fill=colour)


draw = ImageDraw.Draw(img)


# circle([230,230],70,'red')
# rectangle([150,150],50,100,'green')
# circle([700,700],300,'blue')
# line((100,100),(700,100),3,'black')
# line((100,100),(700,200),3,'black')
rectangle(centre=(500, 500), width=150, height=350, angle=17, colour='green')
rectangle(centre=(300, 300), width=200, height=100, angle=23, colour='black')
rectangle(centre=(300,300), width=180, height = 80, angle = 23, colour='black')


img.save('image.png')

