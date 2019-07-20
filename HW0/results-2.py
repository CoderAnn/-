from PIL import Image
import numpy as np
import scipy.misc
img_1 = np.array(Image.open('01-Data/lena.png'))
img_2 = np.array(Image.open('01-Data/lena_modified.png'))
h = np.shape(img_2)[0]
c = np.shape(img_2)[-1]
for i in range(h):
    for j in range(h):
        for k in range(c):
            if img_1[i][j][k] == img_2[i][j][k]:
                img_2[i][j][k] = 255
scipy.misc.imsave('ans_two.png', img_2)



