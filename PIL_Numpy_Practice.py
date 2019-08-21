from PIL import Image
import os
import time
import numpy as np


def create_thumbnail(filename, t_size):
    t_image = Image.open(filename)
    t_image.thumbnail((t_size, t_size))

    save_name = filename.split(".")[0]
    t_image.save(f"{save_name}-thumbnail.png")


def rgb_channel(filename):
    im = Image.open(filename)
    width, height = im.size

    im_red = Image.new("RGB", (width, height))
    im_green = Image.new("RGB", (width, height))
    im_blue = Image.new("RGB", (width, height))

    for x in range(width):
        for y in range(height):
            r, g, b = im.getpixel((x, y))
            im_red.putpixel((x, y), (r, 0, 0))
            im_green.putpixel((x, y), (0, g, 0))
            im_blue.putpixel((x, y), (0, 0, b))

    save_name = filename.split(".")[0]
    im_red.save(f"{save_name}-red.png")
    im_green.save(f"{save_name}-green.png")
    im_blue.save(f"{save_name}-blue.png")


def rgb_numpy(filename):
    im = Image.open(filename)

    red_array = np.array(im)
    green_array = np.array(im)
    blue_array = np.array(im)

    red_array[:, :, 1:3] = 0

    green_array[:, :, 0] = 0
    green_array[:, :, 2] = 0

    blue_array[:, :, 0:2] = 0

    red_im = Image.fromarray(red_array)
    green_im = Image.fromarray(green_array)
    blue_im = Image.fromarray(blue_array)

    save_name = filename.split(".")[0]

    red_im.save(f"{save_name}-red_np.png")
    green_im.save(f"{save_name}-green_np.png")
    blue_im.save(f"{save_name}-blue_np.png")


def gray_scale(filename):
    im = Image.open(filename)
    width, height = im.size

    for x in range(width):
        for y in range(height):
            r, g, b = im.getpixel((x, y))
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            im.putpixel((x, y), (gray, gray, gray))

    save_name = filename.split(".")[0]
    im.save(f"{save_name}-grayscale.png")


def gray_scale_numpy(filename):
    im = Image.open(filename)
    im_array = np.array(im)
    # print(im_array.shape)

    dot_im_array = np.dot(im_array[..., :3], [0.299, 0.587, 0.114])

    im_array[:, :, 0] = dot_im_array[:, :]
    im_array[:, :, 1] = dot_im_array[:, :]
    im_array[:, :, 2] = dot_im_array[:, :]

    im = Image.fromarray(im_array)

    save_name = filename.split(".")[0]
    im.save(f"{save_name}-numpy_grayscale.png")


def mix(filename):
    im = Image.open(filename)
    width, height = im.size
    for x in range(width):
        for y in range(height):
            r, g, b = im.getpixel((x, y))
            im.putpixel((x, y), (g, b, r))
            # im.putpixel((x, y), (b, r, g))

    save_name = filename.split(".")[0]
    im.save(f"{save_name}-mix.png")


def mix_numpy(filename):
    im = Image.open(filename)
    im_array = np.array(im)
    im_array2 = np.array(im_array)

    # make rgb to gbr
    im_array[:, :, 0] = im_array2[:, :, 1]
    im_array[:, :, 1] = im_array2[:, :, 2]
    im_array[:, :, 2] = im_array2[:, :, 0]

    im = Image.fromarray(im_array)

    save_name = filename.split(".")[0]
    im.save(f"{save_name}-mix_numpy.png")


def negative(filename):
    im = Image.open(filename)
    im_array = np.array(im)
    im_array = 255 - im_array
    im = Image.fromarray(im_array)
    save_name = filename.split(".")[0]
    im.save(f"{save_name}-negative.png")

os.chdir(r"C:\Users\Hifas\Desktop\Temp\Images")

s_time = time.clock()

# create_thumbnail("v.jpg", 1200)
# gray_scale("5.png")             # 1.878 seconds
# gray_scale_numpy("8.png")       # 0.238 seconds
# mix("1.png")                    # 1.661 seconds
mix_numpy("4.png")              # 0.205 seconds
# rgb_channel("1.png")            # 3.405 seconds, 14.14 seconds for 1920 x 1080
# rgb_numpy("1.png")              # 0.856 seconds, 3.0865 seconds for 1920 x 1080
# negative("4.png")

print(f"{time.clock() - s_time:0.4f} seconds")

