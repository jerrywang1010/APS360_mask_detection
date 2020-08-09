from PIL import Image, ImageFilter
import random
incorrect_path = "C:\\Users\\jerry\\Downloads\\aps360\\resized_to_224x224\\mask_weared_incorrect\\"
with_mask_path = "C:\\Users\\jerry\\Downloads\\aps360\\resized_to_224x224\\with_mask\\"
without_mask_path = "C:\\Users\\jerry\\Downloads\\aps360\\resized_to_224x224\\without_mask\\"

save_path = "C:\\Users\\jerry\\Downloads\\aps360\\better_augmented\\"

'''
augmentation_index = 0: rotate right 20 degree
augmentation_index = 1: rotate left 20 degree
augmentation_index = 2: horizontal flip
augmentation_index = 3: add Gaussian noise
'''

img = Image.open(without_mask_path + "1.png")
img.show()
img.rotate(20).save('C:\\Users\\jerry\\Desktop\\0.png')
img.rotate(340).save('C:\\Users\\jerry\\Desktop\\1.png')
img.transpose(Image.FLIP_LEFT_RIGHT).save('C:\\Users\\jerry\\Desktop\\2.png')
img.filter(ImageFilter.GaussianBlur(5)).save('C:\\Users\\jerry\\Desktop\\3.png')
incorrect_count = 0
for i in range(123):
    im = Image.open(incorrect_path + str(i) + ".png")
    for j in range(20):
        augmentation_index = random.randint(0, 3)
        if augmentation_index == 0:
            save_image = im.rotate(20)
        elif augmentation_index == 1:
            save_image = im.rotate(340)
        elif augmentation_index == 2:
            save_image = im.transpose(Image.FLIP_LEFT_RIGHT)
        elif augmentation_index == 3:
            save_image = im.filter(ImageFilter.GaussianBlur(5))
        save_image.save(save_path + "mask_weared_incorrect\\" + str(incorrect_count) + ".png")
        incorrect_count += 1

without_mask_count = 0
for i in range(717):
    im = Image.open(without_mask_path + str(i) + ".png")
    for j in range(4):
        augmentation_index = random.randint(0, 3)
        if augmentation_index == 0:
            save_image = im.rotate(20)
        elif augmentation_index == 1:
            save_image = im.rotate(340)
        elif augmentation_index == 2:
            save_image = im.transpose(Image.FLIP_LEFT_RIGHT)
        elif augmentation_index == 3:
            save_image = im.filter(ImageFilter.GaussianBlur(5))
        save_image.save(save_path + "without_mask\\" + str(without_mask_count) + ".png")
        without_mask_count += 1
