# Hi, I'm code kudos, this program converts any image to sketck using python & sketchpy.
## Hope you like it
### To see more like this Subscribe to 
#### Youtube: @codekudos
##### Instagram: @codekudos
###### Twitter: @code_kudos

from sketchpy import canvas
obj = canvas.sketch_from_image('bp.jpg')
obj.draw(threshold = 200)