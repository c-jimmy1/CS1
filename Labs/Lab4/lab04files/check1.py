from PIL import Image
from check2_helper import make_square

im1 = Image.open('ca.jpg')
im2 = Image.open('im.jpg')
im3 = Image.open('hk.jpg')
im4 = Image.open('bw.jpg')

bk = Image.new('RGB', (512,512), 'white')

im1 = make_square(im1)
im2 = make_square(im2)
im3 = make_square(im3)
im4 = make_square(im4)

im1 = im1.resize((256,256))
im2 = im2.resize((256,256))
im3 = im3.resize((256,256))
im4 = im4.resize((256,256))

bk.paste(im1, (0,0))
bk.paste(im2, (0,256))
bk.paste(im3, (256,0))
bk.paste(im4, (256,256))

bk.show()

