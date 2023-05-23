from PIL import Image

im = Image.new('RGB', (512,512))
im = Image.open('ca.jpg')
im.show()