from PIL import Image, ImageDraw
import math

# ---------------------------------------------------
# Utility Functions
# ---------------------------------------------------

# Convert radians to degrees
def radToDeg(radians):
	return (180 / math.pi) * radians

# Convert degrees to radians
def degToRad(degrees):
	return (math.pi / 180) * degrees

# Distance between two points
def dPoints(p1, p2):
	return math.sqrt(math.pow(p1[0]-p2[0], 2) + math.pow(p1[1]-p2[1], 2))

def buildTriangle(Xc, Yc, dLength, alpha, dAlpha):
	x1 = Xc + dLength*math.cos(alpha)
	y1 = Yc + dLength*math.sin(alpha)
	x2 = Xc + dLength*math.cos(alpha + dAlpha)
	y2 = Yc + dLength*math.sin(alpha + dAlpha)
	return ((Xc, Yc), (x1, y1), (x2, y2))
# ---------------------------------------------------
# Global Settings
# ---------------------------------------------------

# ---------------------------------------------------
# Image dims
Xmax = 5000
Ymax = 2500

# Location of beamer
# Xc = 100
# Yc = 50
# Center
Xc = Xmax / 4
Yc = Ymax / 2

# Angle width of beams [degrees] (Beware of artifacts when over ~10 degrees)
dAlphaDeg = 5
dAlpha = degToRad(dAlphaDeg)

# Find the largest chord in the drawing
dCorners = [
	dPoints((Xc, Yc), (0, 0)),
	dPoints((Xc, Yc), (0, Ymax)),
	dPoints((Xc, Yc), (Xmax, 0)),
	dPoints((Xc, Yc), (Xmax, Ymax))
]
dLength = max(dCorners)

N = 360 / dAlphaDeg

### CHOOSE COLORS ###
Color1 = "#fcef60"
Color2 = "#faeb1b"

# Start working
alpha = 0.01

img = Image.new('RGB', (Xmax, Ymax))
draw = ImageDraw.Draw(img)

for i in range(N):
	p0, p1, p2 = buildTriangle(Xc, Yc, dLength, alpha + i*dAlpha, dAlpha)
	if (i % 2 == 0):
		draw.polygon(p0 + p1 + p2, fill=Color1)
	else:
		draw.polygon(p0 + p1 + p2, fill=Color2)

del draw
imgName = "images/img.%d.%dx%d.(%s-%s).jpeg" % (dAlphaDeg, Xmax, Ymax, Color1, Color2)
img.save(imgName, quality=100, optimize=True, progressive=True)
# img.show()