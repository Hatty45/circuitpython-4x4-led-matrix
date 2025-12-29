# Circuitpython 4x4 LED Matrix
## What it does
This code makes a 4x4 LED Matrix display 4x4 images (ideally a good beginner project on breadboards)

## Schematic
<img width="1317" height="720" alt="image" src="https://github.com/user-attachments/assets/6ca3fa05-8d7d-4757-8c89-fbe942a1b827" />
<strong>NOTE:</strong> the row pins MUST be wired into the LED's Anodes, and the columns' into the Cathodes.

## Usage
Simply create a 4x4 'image' (a 4x4 array) or a 'long image' (an ?x4 array), and either:
* For images, just use the ```draw```/```holddraw``` function
* For long images, just use the same functions but use the ```getfraction``` function to get the right part to render

## Functions
| Function | Usage |
|----------|-------|
| ```draw(image, delay)``` | Renders the ```image``` to the display, with the ```delay``` of rendering the individual rows |
| ```holddraw(image, time)``` | Draws the ```image``` for ```time``` seconds |
| ```getfraction(full, xpos)``` | Gets a regular image from the ```full``` full-image, with the started chosen x-position (```xpos```) and another 3 across |

## Example
(This exaple will be used as if the code in ```code.py``` (the file here) was in another file in the ```CIRCUITPY``` directory. I have called it ```matrix.py```)

```
import matrix

# in case you can't read it, it says "matrix"
fullword = (
    (0,0,0,0,1,0,0,0,1,0,0,1,0,0,1,1,1,0,1,1,0,0,1,1,1,0,1,0,1,0,0,0,0),
    (0,0,0,0,1,1,0,1,1,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,0,1,0,0,0,0,0),
    (0,0,0,0,1,0,1,0,1,0,1,1,1,0,0,1,0,0,1,1,0,0,0,1,0,0,1,0,1,0,0,0,0),
    (0,0,0,0,1,0,0,0,1,0,1,0,1,0,0,1,0,0,1,0,1,0,1,1,1,0,1,0,1,0,0,0,0)
)

index = 0 # where to start displaying the image from
imagelength = len(fullword[0])-4 # length of image

delay = 0.05 # scroll delay in seconds

while True:
    holddraw(getfraction(fullword,index),delay*1000) # draws one 'fraction' of the full image
    index = (index+1)%imagelength # moves to the next x-position
```
