from PIL import Image, ImageDraw
import math
from itertools import cycle

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

# Image dims
Xmax = 5000
Ymax = 2500

# Location of beamer
Xc = Xmax / 2
Yc = Ymax / 2

# Colors
Colors = [
	"#fcef60",
	"#faeb1b",
]
colorsPool = cycle(Colors)

# Angle width of beams [degrees]
dAlphaDeg = 5

# ---------------------------------------------------
# Initialization
# ---------------------------------------------------

# Set dAlpha in radians
dAlpha = degToRad(dAlphaDeg)

# Find the largest chord in the drawing
dCorners = [
	dPoints((Xc, Yc), (0, 0)),
	dPoints((Xc, Yc), (0, Ymax)),
	dPoints((Xc, Yc), (Xmax, 0)),
	dPoints((Xc, Yc), (Xmax, Ymax))
]
dCornerLength = max(dCorners)
dLength = dCornerLength / (math.sin(dAlpha / 2))

# Set number of rays
N = 360 / dAlphaDeg + 1

# Minimal start angle
alpha = 0.0001

# ---------------------------------------------------
# Main Program
# ---------------------------------------------------

# Init img and draw
img = Image.new('RGB', (Xmax, Ymax))
draw = ImageDraw.Draw(img)

# Draw beams
for i in range(N):
	p0, p1, p2 = buildTriangle(Xc, Yc, dLength, alpha + i*dAlpha, dAlpha)
	draw.polygon(p0 + p1 + p2, fill=colorsPool.next())

# Clean up
del draw

# Save or Show file
imgName = "images/img.%d.%dx%d.jpeg" % (dAlphaDeg, Xmax, Ymax)
img.save(imgName, quality=100, optimize=True, progressive=True)
# img.show()

# ---------------------------------------------------