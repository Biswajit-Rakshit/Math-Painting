from canvas import Canvas
from shapes import Rectangle,Square

# Get canvas width and height from the user
canvasHeight = int(input("Enter Canvas Height : "))
canvasWidth = int(input("Enter Canvas Width : "))

# Make a dictionary of color codes and prompts for color
colors = {"white": (255,255,255), "black": (0,0,0)}
while True:
    canvasColor = input("Enter Canvas color (white/black) : ")
    if canvasColor.lower() not in ['black','white']:
        print("Please select between (black/white)")
        continue
    else:
        canvasColor = canvasColor.lower()
        break

# Create a canvas with the user data
canvas = Canvas(height=canvasHeight,width=canvasWidth,color=colors[canvasColor])

while True:
    shapeType = input("What do you like to draw ? Enter quit to quit. :")
    # Ask for Rectangle data and create rectangle if user entered 'rectangle'
    if shapeType.lower() == 'rectangle':
        rectangleX = int(input("Enter x of the Rectangle : "))
        rectangleY = int(input("Enter y of the Rectangle : "))
        rectangleWidth = int(input("Enter Width of the Rectangle : "))
        rectangleHeight = int(input("Enter Height of the Rectangle : "))
        red = int(input("How much red should the rectangle have : "))
        green = int(input("How much green :"))
        blue = int(input("How much blue :"))

        # Create the rectangle
        r1 = Rectangle(x=rectangleX,y=rectangleY,height=rectangleHeight,width=rectangleWidth,color=(red,green,blue))
        r1.draw(canvas)

    if shapeType.lower() == 'square':
        squareX = int(input("Enter x of the square : "))
        squareY = int(input("Enter y of the square : "))
        squareSide = int(input("Enter the side of the square : "))
        red = int(input("How much red should the square have : "))
        green = int(input("How much green :"))
        blue = int(input("How much blue :"))

        # Create the square
        s1 = Square(x=squareX,y=squareY,side=squareSide,color=(red,green,blue))
        s1.draw(canvas)

    # Break the loop if user entered 'quit'
    if shapeType.lower() == 'quit':
        break

    else:
        print("Wrong input. Please select (square/rectangle)")

canvas.make('Canvas.png')














# canvas = Canvas(height=28,width=30,color=(255,255,255))
# r1 = Rectangle(x=1,y=6,height=7,width=10,color=(100,200,125))
# r1.draw(canvas)
# s1 = Square(x=1,y=3,side=3,color=(0,100,222))
# s1.draw(canvas)
# canvas.make('canvas.png')