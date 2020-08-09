from PIL import Image
import xml.etree.ElementTree as ET

# calculate min_size max_size for each class of cropped images
incorrect_path = "C:\\Users\\jerry\\Downloads\\aps360\\processed\\mask_weared_incorrect"

min_width = float("inf")
max_width = 0
min_height = float("inf")
max_height = 0
max_ratio = 0
min_ratio = float("inf")
total_width = 0
total_height = 0
for i in range(123):
    im = Image.open(incorrect_path + "\\" + str(i) + ".png")
    size = im.size
    total_width += size[0]
    total_height += size[1]
    if size[0] < min_width:
        min_width = size[0]
    elif size[0] > max_width:
        max_width = size[0]
    if size[1] < min_height:
        min_height = size[1]
    elif size[1] > max_height:
        max_height = size[1]
    w_h_ratio = size[0] / size[1]
    if w_h_ratio < min_ratio:
        min_ratio = w_h_ratio
    elif w_h_ratio > max_ratio:
        max_ratio = w_h_ratio
print("for all mask_weared_incorrectly images, min_width={}, max_width={}, min_height={}, max_height={}, min_w/h_ratio={}, max_w/h_ratio={}".format(min_width, max_width, min_height, max_height, min_ratio, max_ratio))


with_mask_path = "C:\\Users\\jerry\\Downloads\\aps360\\processed\\with_mask"
# min_width = float("inf")
# max_width = 0
# min_height = float("inf")
# max_height = 0
# max_ratio = 0
# min_ratio = float("inf")
for i in range(3232):
    im = Image.open(with_mask_path + "\\" + str(i) + ".png")
    size = im.size
    total_width += size[0]
    total_height += size[1]
    if size[0] < min_width:
        min_width = size[0]
    elif size[0] > max_width:
        max_width = size[0]
    if size[1] < min_height:
        min_height = size[1]
    elif size[1] > max_height:
        max_height = size[1]
    w_h_ratio = size[0] / size[1]
    if w_h_ratio < min_ratio:
        min_ratio = w_h_ratio
    elif w_h_ratio > max_ratio:
        max_ratio = w_h_ratio
print("for all with_mask images, min_width={}, max_width={}, min_height={}, max_height={}, min_w/h_ratio={}, max_w/h_ratio={}".format(min_width, max_width, min_height, max_height, min_ratio, max_ratio))



without_mask_path = "C:\\Users\\jerry\\Downloads\\aps360\\processed\\without_mask"
# min_width = float("inf")
# max_width = 0
# min_height = float("inf")
# max_height = 0
# max_ratio = 0
# min_ratio = float("inf")
for i in range(717):
    im = Image.open(without_mask_path + "\\" + str(i) + ".png")
    size = im.size
    total_width += size[0]
    total_height += size[1]
    if size[0] < min_width:
        min_width = size[0]
    elif size[0] > max_width:
        max_width = size[0]
    if size[1] < min_height:
        min_height = size[1]
    elif size[1] > max_height:
        max_height = size[1]
    w_h_ratio = size[0] / size[1]
    if w_h_ratio < min_ratio:
        min_ratio = w_h_ratio
    elif w_h_ratio > max_ratio:
        max_ratio = w_h_ratio
print("for all without_mask images, min_width={}, max_width={}, min_height={}, max_height={}, min_w/h_ratio={}, max_w/h_ratio={}".format(min_width, max_width, min_height, max_height, min_ratio, max_ratio))
avg_width = total_width / (717 + 3232 + 123)
avg_height = total_height / (717 + 3232 + 123)
print("avg_width = {}, avg_height={}".format(avg_width, avg_height))
