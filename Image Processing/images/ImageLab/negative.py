
from PIL import Image, ImageOps
im = Image.open('horse.png').convert('RGB')
im_invert = ImageOps.invert(im)
im_invert.save('horse_invert.png')