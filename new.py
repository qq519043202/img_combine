import skimage.io
import skimage.transform
import numpy as np

white = "font.jpg"
black = "back.jpg"

def resize(img, width=200, height=200):
	return skimage.transform.resize(img, (width, height))


white_img = skimage.io.imread(white, as_grey=True)
# , as_grey=True)
black_img = skimage.io.imread(black, as_grey=True)
# , as_grey=True)

width1, height1 = white_img.shape
width2, height2 = black_img.shape

width = min(width1, width2)
height = min(height1, height2)


white_img = resize(white_img, width, height)/2
black_img = resize(black_img, width, height)/2+0.5

a1 = 1 - white_img * 2

a2 = (black_img - 0.5) * 2

white_img_png = np.zeros((width, height,4))
black_img_png = np.zeros((width, height,4))

new_img_png = np.zeros((width, height,4))

# white_img_png[:,:,0] = white_img
# white_img_png[:,:,1] = white_img
# white_img_png[:,:,2] = white_img
# white_img_png[:,:,3] = a1

a3 = (a1+a2) / 2
g3 = (a2 - a1)/2 + 0.5
new_img_png[:,:,3] = a3
new_img_png[:,:,0] = g3
new_img_png[:,:,1] = g3
new_img_png[:,:,2] = g3


skimage.io.imsave("new2.png",new_img_png)
# skimage.io.imsave("new-b1.png",black_img/2)
