"""
import os
from PIL import Image

supported = ['jpeg', 'jpg', 'png']

def resize_images():
    crop_frame = (0, 0, 1280, 800);
    image_dir = os.getcwd()+'/opal/static/images/slideshow/'
    img_list = os.listdir(image_dir)
    rs_image_dir = os.getcwd()+'/opal/static/images/slideshow/resized/'
    rs_img_list = os.listdir(rs_image_dir)
    images = ['images/slideshow/'+filename for filename in os.listdir(image_dir)]
    for img in img_list:
        if not img in rs_img_list:
            try:
              im = Image.open(image_dir+img)
              crop_im = im.crop(crop_frame).resize((1920,1200)).save(rs_image_dir+img)
            except:
              continue
resize_images()
"""
