
from PIL import Image

im1 = Image.open('1.jpg')
im2 = Image.open('2.jpg')
im3 = Image.open('3.jpg')
im4 = Image.open('4.jpg')
im5 = Image.open('5.jpg')
im6 = Image.open('6.jpg')

bk = Image.new('RGB', (1000,360))


im1 = im1.resize((149,256))
im2 = im2.resize((149,256))
im3 = im3.resize((149,256))
im4 = im4.resize((149,256))
im5 = im5.resize((149,256))
im6 = im6.resize((149,256))

bk.paste(im1, (31,21))
bk.paste(im2, (189,81))
bk.paste(im3, (347,21))
bk.paste(im4, (505,81))
bk.paste(im5, (663,21))
bk.paste(im6, (821,81))


bk.show()