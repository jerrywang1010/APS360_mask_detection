from PIL import Image
incorrect_path = "C:\\Users\\jerry\\Downloads\\aps360\\resized_to_224x224\\mask_weared_incorrect\\"
with_mask_path = "C:\\Users\\jerry\\Downloads\\aps360\\resized_to_224x224\\with_mask\\"
without_mask_path = "C:\\Users\\jerry\\Downloads\\aps360\\resized_to_224x224\\without_mask\\"
save_path = "C:\\Users\\jerry\\Downloads\\aps360\\augmented\\"

incorrect_count = 0
for i in range(123):
    im = Image.open(incorrect_path + str(i) + ".png")
    for j in range(20):
        im.save(save_path + "mask_weared_incorrect\\" + str(incorrect_count) + ".png")
        incorrect_count += 1

without_mask_count = 0
for i in range(717):
    im = Image.open(without_mask_path + str(i) + ".png")
    for j in range(4):
        im.save(save_path + "without_mask\\" + str(without_mask_count) + ".png")
        without_mask_count += 1
