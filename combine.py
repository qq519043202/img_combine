import skimage.io
import skimage.transform
import numpy as np

white = "font.jpg"
black = "back.jpg"

def resize(img, size=200):
	return skimage.transform.resize(img, (size, size))


white_img = resize(skimage.io.imread(white, as_grey=True))
black_img = resize(skimage.io.imread(black, as_grey=True))

white_img_png = np.zeros((200,200,4))
black_img_png = np.zeros((200,200,4))
new_img_png = np.zeros((200,200,4))

for x in range(0,200):
	for y in range(0,200):
		g1 = white_img[x,y] * 255 / 2
		g2 = black_img[x,y] * 255 / 2
		if g1 > 64:
			white_img_png[x,y,3] = 0
			white_img_png[x,y,0:3] = 0
		else:
			white_img_png[x,y,3] = 255
			white_img_png[x,y,0:3] = 0
		if g2 > 64:
			black_img_png[x,y,3] = 255
			black_img_png[x,y,0:3] = 255
		else:
			black_img_png[x,y,3] = 0
			black_img_png[x,y,0:3] = 0


		if white_img_png[x,y,3] >= 250 and black_img_png[x,y,3] >=250:
			new_img_png[x,y,3] = 255
			new_img_png[x,y,0:3] = 128
		elif white_img_png[x,y,3] >= 250 and black_img_png[x,y,3] <=5:
			new_img_png[x,y,3] = 128
			new_img_png[x,y,0:3] = 0
		elif white_img_png[x,y,3] <= 5 and black_img_png[x,y,3] <=5:
			new_img_png[x,y,3] = 0
			new_img_png[x,y,0:3] = 128
		else:
			new_img_png[x,y,3] = 128
			new_img_png[x,y,0:3] = 255

skimage.io.imsave("result.png",new_img_png/255)
