from PIL import Image
incorrect_path = "C:\\Users\\jerry\\Downloads\\aps360\\processed\\mask_weared_incorrect\\"
without_mask_path = "C:\\Users\\jerry\\Downloads\\aps360\\processed\\without_mask\\"
with_mask_path = "C:\\Users\\jerry\\Downloads\\aps360\\processed\\with_mask\\"
save_path = "C:\\Users\\jerry\\Downloads\\aps360\\resized_to_224x224\\"

size = (224, 224)
for i in range(123):
    im = Image.open(incorrect_path + str(i) + ".png")
    im_resized = im.resize(size)
    im_resized.save(save_path + "mask_weared_incorrect\\" + str(i) + ".png")

for i in range(3232):
    im = Image.open(with_mask_path + str(i) + ".png")
    im_resized = im.resize(size)
    im_resized.save(save_path + "with_mask\\" + str(i) + ".png")

for i in range(717):
    im = Image.open(without_mask_path + str(i) + ".png")
    im_resized = im.resize(size)
    im_resized.save(save_path + "without_mask\\" + str(i) + ".png")