from PIL import Image, ImageFilter, ImageDraw
import os
import random
import numpy as np

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def blur(num):
    save_path = '/Users/samin/Desktop/Classes/9.60/9.60-Project/new_datasets/adversarial_dataset/blur/images'
    ensure_dir(save_path)
    original_image = Image.open(f"/Users/samin/Desktop/Classes/9.60/9.60-Project/new_datasets/adversarial_dataset/images/{num}")
    blurred_image = original_image.filter(ImageFilter.BLUR)
    blurred_image.save(f'{save_path}/{num}')

def shift(num):
    save_path = '/Users/samin/Desktop/Classes/9.60/9.60-Project/new_datasets/adversarial_dataset/shift/images'
    ensure_dir(save_path)
    img = Image.open(f"/Users/samin/Desktop/Classes/9.60/9.60-Project/new_datasets/adversarial_dataset/images/{num}")
    hsv_img = img.convert('HSV')
    pixels = list(hsv_img.getdata())
    newpixels = []
    for pixel in pixels:
        newpixels.append((int((pixel[0] + (255 * 350) / 360) % 255), pixel[1], pixel[2]))

    shifted_hsv_img = Image.new('HSV', img.size)
    shifted_hsv_img.putdata(newpixels)
    shifted_img = shifted_hsv_img.convert('RGB')
    shifted_img.save(f'{save_path}/{num}')

def rotate(num):
    save_path = '/Users/samin/Desktop/Classes/9.60/9.60-Project/new_datasets/adversarial_dataset/rotate/images'
    ensure_dir(save_path)
    with Image.open(f"/Users/samin/Desktop/Classes/9.60/9.60-Project/new_datasets/adversarial_dataset/images/{num}") as img:
        x = random.randint(135, 225)
        rotated_img = img.rotate(x, expand=True, resample=Image.BICUBIC)
        rotated_img.save(f'{save_path}/{num}')

def flip(num):
    save_path = '/Users/samin/Desktop/Classes/9.60/9.60-Project/new_datasets/adversarial_dataset/flip/images'
    ensure_dir(save_path)
    with Image.open(f"/Users/samin/Desktop/Classes/9.60/9.60-Project/new_datasets/adversarial_dataset/images/{num}") as img:
        # Rotate the image by 180 degrees
        rotated_img = img.rotate(180, expand=True, resample=Image.BICUBIC)
        rotated_img.save(f'{save_path}/{num}')


def create_radial_mask(size, center, radius, spread):
    mask = Image.new('L', size, 255)
    draw = ImageDraw.Draw(mask)
    for y in range(size[1]):
        for x in range(size[0]):
            distance = np.sqrt((x - center[0]) ** 2 + (y - center[1]) ** 2)
            opacity = np.exp(-distance / spread) * 255
            draw.point((x, y), fill=int(opacity))
    return mask

def apply_mask(image, mask):
    mask = mask.convert('RGB')
    np_image = np.array(image)
    np_mask = np.array(mask) / 255
    darkened_image = (np_image * np_mask).astype(np.uint8)
    darkened_image = Image.fromarray(darkened_image, 'RGB')
    return darkened_image

def darken(num):
    save_path = '/Users/samin/Desktop/Classes/9.60/9.60-Project/new_datasets/adversarial_dataset/darken/images'
    ensure_dir(save_path)
    image = Image.open(f'/Users/samin/Desktop/Classes/9.60/9.60-Project/new_datasets/adversarial_dataset/images/{num}')
    center = (image.width // 2, image.height // 2)
    radius = min(center)
    spread = 100
    mask = create_radial_mask(image.size, center, radius, spread)
    darkened_image = apply_mask(image, mask)
    darkened_image.save(f'{save_path}/{num}')

# Sample usage with directory creation
directory = '/Users/samin/Desktop/Classes/9.60/9.60-Project/new_datasets/adversarial_dataset/images'
for file in os.listdir(directory):
    flip(file)
#     # darken(file)
#     blur(file)
#     shift(file)
#     rotate(file)

# def ensure_dir(path):
#     os.makedirs(path, exist_ok=True)

# def shift(num, hue_shift):
#     save_path = f'/Users/samin/Desktop/Classes/9.60/9.60-Project/new_datasets/adversarial_dataset/shift-{hue_shift}/images'
#     ensure_dir(save_path)
#     img = Image.open(f"/Users/samin/Desktop/Classes/9.60/9.60-Project/new_datasets/adversarial_dataset/images/{num}")
#     hsv_img = img.convert('HSV')
#     pixels = list(hsv_img.getdata())
#     newpixels = []
#     for pixel in pixels:
#         new_hue = (pixel[0] + (255 * hue_shift) / 360) % 255
#         newpixels.append((int(new_hue), pixel[1], pixel[2]))

#     shifted_hsv_img = Image.new('HSV', img.size)
#     shifted_hsv_img.putdata(newpixels)
#     shifted_img = shifted_hsv_img.convert('RGB')
#     shifted_img.save(f'{save_path}/{num}')

# # Sample usage with directory creation and varying shift values
# shift_values = [40, 80, 120, 160, 200, 240, 280, 320, 350]
# for file in os.listdir(directory):
#     for value in shift_values:
#         shift(file, value)

