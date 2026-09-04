from PIL import Image
import numpy as np
#image of the topo map
image = Image.open("Topo map2.jpg")

def crop_image(image):
    #crop the image, so that its sides can be divisable by 10
    dimensions = (0, 0, image.size[0] - image.size[0]%10, image.size[1] - image.size[1]%10)

    crop_i = image.crop(dimensions)
    print(crop_i.size)
    return crop_i

def find_avg_rgb(array):
    #given a specific region, find the average value of the color in the region
    r = 0
    g = 0
    b = 0
    t = 0
    for y in array:
        for x in y:
            t += 1
            r += x[0]
            g += x[1]
            b += x[2]
    r /= t
    g /= t
    b /= t

    
    return (r, g, b)

def find_close_color(rgb, color_list):
    color = (0, 0, 0)
    t = 600
    for i in color_list:
        if abs(int(sum(rgb)) - sum(i)) < t:
            color = i
            t = abs(int(sum(rgb)) - sum(i))
    return color


def seperate_region(image):
    #given a specific image, seperate the image into 10-10 pixel regions
    regions = {}
    
    for x in range(0, image.size[0], 5):
        for y in range(0, image.size[1], 5):
            dimensions = (x, y, x + 5, y + 5)
            cropped = image.crop(dimensions)
            color_list = [(190, 190, 190), (130, 160, 130), (140, 180, 120), (0, 0, 0)]
            #color_list = [(180, 180, 180), (50, 250, 50), (120, 250, 120), (0, 0, 0)]
            #540 (white), 350(green), 490( light green), 0 (black)
            #colors used to map the vegetation
            rgb = find_close_color(find_avg_rgb(np.array(cropped)), color_list)
            coordinate = (x, y)
            regions[coordinate] = rgb
            block = Image.new('RGB', (5, 5), color = (int(rgb[0]), int(rgb[1]), int(rgb[2])))
            image.paste(block, dimensions)
    return regions

image.show()
image = crop_image(image)
regions = seperate_region(image)
image.show()

white = 0
light_green = 0
green = 0

for i in regions.values():
    if i == (190, 190, 190):
        white += 1
    elif i == (130, 160, 130):
        green += 1
    elif i == (140, 180, 120):
        light_green += 1

#1 block = 290 m^2

print(f"plains: {white} forest: {light_green} wetland: {green}")
print(f"Crops percentage: {white/(white + light_green + green)}")
print(f"Forest: {light_green/(white + light_green + green)}")
print(f"Wetland: {green/(white + light_green + green)}")
