import argparse
from tqdm import tqdm
from PIL import Image


def convert(name, flag):
    img = Image.open(name)
    width, height = img.size
    img = img.convert('L').convert('RGBA')
    for h in tqdm(range(height)):
        for w in range(width):
            pix = img.getpixel((w, h))
            color = pix[0]
            if flag == 'white':
                img.putpixel((w, h), (color, color, color, 255 - color))
            else:
                img.putpixel((w, h), (color, color, color, color))
    return img


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Input the name of surface image and hidden image.')
    parser.add_argument('surface_image', type=str)
    parser.add_argument('hidden_image', type=str)
    args = parser.parse_args()
    surface_img = args.surface_image
    hidden_img = args.hidden_image

    img1 = convert(surface_img, 'white')
    img2 = convert(hidden_img, 'black')

    if img1.size != img2.size:
        img1_width, img1_height = img1.size
        img2_width, img2_height = img2.size
        width = (img1_width + img2_width) // 2
        height = (img1_height + img2_height) // 2
        img1 = img1.resize((width, height))
        img2 = img2.resize((width, height))

    final_img = Image.blend(img1, img2, 0.4)
    final_img.save('tank.png')
