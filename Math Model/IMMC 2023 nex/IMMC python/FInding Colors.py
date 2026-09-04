from PIL import Image
import numpy as np

forest = Image.open("Forest.jpg")
wetland = Image.open("Wetland.jpg")
crops = Image.open("Crops.jpg")

print(forest.size)
print(np.array(forest))
#(140, 180 120)

print(wetland.size)
print(np.array(wetland))
#(120, 160, 120)

print(crops.size)
print(np.array(crops))
#(210, 210, 210)
