from PIL import Image

def make_square(image):
    w = image.width
    h = image.height
    
    if w < h:
        new = image.crop((0,0,w,w))
    else:
        new = image.crop((0,0,h,h))
    return new


    