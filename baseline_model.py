from PIL import Image
import math
from collections import defaultdict
with_mask_path = "C:\\Users\\jerry\\Downloads\\aps360\\resized_to_224x224\\with_mask\\"
without_mask_path = "C:\\Users\\jerry\\Downloads\\aps360\\resized_to_224x224\\without_mask\\"
incorrect_path = "C:\\Users\\jerry\\Downloads\\aps360\\resized_to_224x224\\mask_weared_incorrect\\"
# example.show()


def distance_from_color(target, color):
    rmean = (target[0] + color[0]) / 2
    r = target[0] - color[1]
    g = target[1] - color[1]
    b = target[2] - color[2]
    return math.sqrt((int(((512 + rmean) * r * r)) >> 8) + 4 * g * g + (int(((767 - rmean) * b * b)) >> 8))


def detect_nose(example_path, threshold=75, skin_count_threshold=500):
    example = Image.open(example_path)
    skin = (174, 128, 107)
    length = 45
    corner1 = (89, 45)
    corner2 = (45, 89)
    skin_count = 0
    for x in range(corner1[0], corner1[0] + length):
        for y in range(corner1[1], corner1[1] + length):
            pixels = example.load()
            band = pixels[x, y]
            # r, g, b = example.getpixel((x, y))
            r = band[0]
            g = band[1]
            b = band[2]
            distance_from_skin = distance_from_color(skin, (r, g, b))
            if distance_from_skin <= threshold:
                skin_count += 1

    for x in range(corner2[0], corner2[0] + 3 * length):
        for y in range(corner2[1], corner2[1] + length):
            pixels = example.load()
            band = pixels[x, y]
            # r, g, b = example.getpixel((x, y))
            r = band[0]
            g = band[1]
            b = band[2]
            distance_from_skin = distance_from_color(skin, (r, g, b))
            if distance_from_skin <= threshold:
                skin_count += 1
    if skin_count >= skin_count_threshold:
        return True
    else:
        return False

def classify(example_path, min_vote=5, detect_nose_threshold=75, detect_nose_count_threshold=500):
    example = Image.open(example_path)
    white = (233, 237, 240)
    black = (20, 20, 20)
    blue = (144, 183, 213)
    green = (120, 177, 150)
    pink = (127, 94, 182)
    skin = (182, 140, 120)

    white_threshold = 100
    black_threshold = 55
    blue_threshold = 100
    green_threshold = 80
    pink_threshold = 100
    skin_threshold = 75

    bound_box = (37, 47)
    start_pos = [56, 80]

    colors = ["white", "black", "blue", "green", "pink", "skin"]
    box_vote = []
    for i in range(3):
        for j in range(3):
            color_count = []
            white_count = 0
            black_count = 0
            blue_count = 0
            green_count = 0
            pink_count = 0
            skin_count = 0
            for x in range(start_pos[0] + i * bound_box[0], start_pos[0] + (i + 1) * bound_box[0]):
                for y in range(start_pos[1] + j * bound_box[1], start_pos[1] + (j + 1) * bound_box[1]):
                    pixels = example.load()
                    band = pixels[x, y]
                    # r, g, b = example.getpixel((x, y))
                    r = band[0]
                    g = band[1]
                    b = band[2]
                    distance_from_white = distance_from_color(white, (r, g, b))
                    distance_from_black = distance_from_color(black, (r, g, b))
                    distance_from_blue = distance_from_color(blue, (r, g, b))
                    distance_from_green = distance_from_color(green, (r, g, b))
                    distance_from_pink = distance_from_color(pink, (r, g, b))
                    distance_from_skin = distance_from_color(skin, (r, g, b))
                    # print("(x,y)={},{}  distance_from_black={}".format(x, y, distance_from_black))
                    if distance_from_white < white_threshold:
                        white_count += 1
                    if distance_from_black < black_threshold:
                        black_count += 1
                    if distance_from_blue < blue_threshold:
                        blue_count += 1
                    if distance_from_green < green_threshold:
                        green_count += 1
                    if distance_from_pink < pink_threshold:
                        pink_count += 1
                    if distance_from_skin < skin_threshold:
                         skin_count += 1
            # print("white_count={}, black_count={}, blue_count={}, green_count={}, pink_count={}, skin_count={}".format(white_count, black_count, blue_count, green_count, pink_count, skin_count))
            color_count.extend([white_count, black_count, blue_count, green_count, pink_count, skin_count])
            major_color = colors[color_count.index(max(color_count))]
            # print("major color = ", major_color)
            box_vote.append(major_color)

    # detect nose to check if weared mask correctly
    found_nose = detect_nose(example_path, threshold=detect_nose_threshold, skin_count_threshold=detect_nose_count_threshold)

    d = defaultdict(int)
    for color in box_vote:
        d[color] += 1
    result = max(d.items(), key=lambda x: x[1])
    # print(result)
    example.close()
    if result[1] >= min_vote-1 and d["skin"] <= 5 and not found_nose:
        return "with_mask", result
    elif result[1] >= min_vote and d["skin"] <= 4 and found_nose:
        return "mask_weared_incorrect", result
    else:
        return "without_mask", result


with_mask_correct = 0
without_mask_correct = 0
incorrect_correct = 0
with_mask_size = 3232
without_mask_size = 717
incorrect_size = 123
for i in range(with_mask_size):
    example_path = with_mask_path + str(i) + ".png"
    result, major_color = classify(example_path, 5)
    if result == "with_mask":
        with_mask_correct += 1
    else:
        print("image: {}, classified as {}, major_color={}".format(example_path, result, major_color))

print("\n")
for i in range(without_mask_size):
    example_path = without_mask_path + str(i) + ".png"
    result, major_color = classify(example_path, 5)
    if result == "without_mask":
        without_mask_correct += 1
    else:
        print("image: {}, classified as {}, major_color={}".format(example_path, result, major_color))

print("\n")
for i in range(incorrect_size):
    example_path = incorrect_path + str(i) + ".png"
    result, major_color = classify(example_path, 5, detect_nose_threshold=100, detect_nose_count_threshold=400)
    if result == "mask_weared_incorrect":
        incorrect_correct += 1
    else:
        print("image: {}, classified as {}, major_color={}".format(example_path, result, major_color))

print("accuracy in with_mask_data = {}".format(with_mask_correct/with_mask_size))
print("accuracy in without_mask_data = {}".format(without_mask_correct/without_mask_size))
print("accuracy in mask_weared_incorrect_data = {}".format(incorrect_correct / incorrect_size))



# for i in range(incorrect_size):
#     example_path = incorrect_path + str(i) + ".png"
#     result = detect_nose(example_path, threshold=100, skin_count_threshold=500)
#     if result:
#         incorrect_correct += 1
#     else:
#         print("image: {} not found nose".format(example_path))
# print("accuracy in mask_weared_incorrect_data = {}".format(incorrect_correct / incorrect_size))
