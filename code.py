"""
 === 4x4 LED MATRIX (by MopsicleKeebs) ===

 - an image is a 4x4 array with 1s/0s to display a picture
 
 - pin selection: 
     > the row pins start from top to bottom
     > the column pins start from right to left
"""

import digitalio, board, time # import main modules

# columns
c0 = digitalio.DigitalInOut(board.GP0) # GPIO pin for column 0
c1 = digitalio.DigitalInOut(board.GP1) # GPIO pin for column 1
c2 = digitalio.DigitalInOut(board.GP2) # GPIO pin for column 2 
c3 = digitalio.DigitalInOut(board.GP3) # GPIO pin for column 3

# set column pins to output
c0.direction = digitalio.Direction.OUTPUT
c1.direction = c0.direction
c2.direction = c1.direction
c3.direction = c2.direction

# rows
r0 = digitalio.DigitalInOut(board.GP4) # GPIO pin for row 0
r1 = digitalio.DigitalInOut(board.GP5) # GPIO pin for row 1
r2 = digitalio.DigitalInOut(board.GP6) # GPIO pin for row 2
r3 = digitalio.DigitalInOut(board.GP7) # GPIO pin for row 3

# set row pins to output
r0.direction = digitalio.Direction.OUTPUT
r1.direction = r0.direction
r2.direction = r1.direction
r3.direction = r2.direction

# create list for easier access to rows
rs = (r0, r1, r2, r3)

# NOTE: 

# draw image to display
def draw(image, delay):
    for r in range(4):
        rs[r].value = 0 # enable the row
            
        # enable the columns
        c3.value = image[r][0]
        c2.value = image[r][1]
        c1.value = image[r][2]
        c0.value = image[r][3]
        
        # wait for refresh and disable the row
        time.sleep(delay/1000)
        rs[r].value = 1
        
        # disable all of the columns, to avoid issues with pixels being left behind
        c3.value = c2.value = c1.value = c0.value = 0
        
# to keep an image on screen for a certain amount of time
def holddraw(image, time):
    for i in range(time):
        draw(image,1)

# gets a 4x4 square of a long image
def getfraction(full,xpos):
    return (
        full[0][xpos:xpos+4],
        full[1][xpos:xpos+4],
        full[2][xpos:xpos+4],
        full[3][xpos:xpos+4]
        )
