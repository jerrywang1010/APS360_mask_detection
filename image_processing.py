from PIL import Image
import xml.etree.ElementTree as ET

image_path = "C:\\Users\\jerry\\Downloads\\aps360\\images"
save_image_path = "C:\\Users\\jerry\\Downloads\\aps360\\processed"
annotation_path = "C:\\Users\\jerry\\Downloads\\aps360\\annotations"
with_mask_count = 0
without_mask_count = 0
mask_weared_incorrect_count = 0


# crop and generate process images
for i in range(853):
    annotation = annotation_path + "\\maksssksksss" + str(i) + ".xml"
    tree = ET.parse(annotation)
    root = tree.getroot()
    image_name = root[1].text
    im_original = Image.open(image_path + "\\maksssksksss" + str(i) + ".png")
    print("processing image:", image_name)
    for object in root.findall('object'):
        type = object.find('name').text
        bound_box = object.find('bndbox')
        xmin = int(bound_box.find('xmin').text)
        ymin = int(bound_box.find('ymin').text)
        xmax = int(bound_box.find('xmax').text)
        ymax = int(bound_box.find('ymax').text)
        print("type={}, xmin={}, ymin={}, xmax={}, ymax={}".format(type, xmin, ymin, xmax, ymax))
        im_cropped = im_original.crop((xmin, ymin, xmax, ymax))
        if type == "with_mask":
            im_cropped.save(save_image_path + "\\with_mask\\" + str(with_mask_count) + ".png")
            with_mask_count += 1
        elif type == "without_mask":
            im_cropped.save(save_image_path + "\\without_mask\\" + str(without_mask_count) + ".png")
            without_mask_count += 1
        elif type == "mask_weared_incorrect":
            im_cropped.save(save_image_path + "\\mask_weared_incorrect\\" + str(mask_weared_incorrect_count) + ".png")
            mask_weared_incorrect_count += 1

