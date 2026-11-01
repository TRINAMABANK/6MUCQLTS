from PIL import Image

im = Image.open('print_preview_test.png')
# Crop the top header area of the A4 sheet
# A4 sheet is centered in 1200px window
w, h = im.size
crop_area = (int(w * 0.25), 50, int(w * 0.75), 320)
cropped = im.crop(crop_area)
cropped.save('header_crop.png')
print('Cropped successfully, size:', cropped.size)
