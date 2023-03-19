from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps
import cv2
import numpy as np
def shadow(text="hello",fontsize=200,image_url='image.jpg'):
    # Some input images
    image = Image.open(image_url).resize((1920, 1080))

    font = ImageFont.truetype('uni-sans.heavy-caps.otf', fontsize)
    draw = ImageDraw.Draw(image)
    text_width, text_height = draw.textsize(text, font)
    x = (1920 - text_width) / 2
    y = (1080 - text_height) / 2

    # Create a new alpha channel
    alpha = Image.new('L', (1920, 1080))
    draw_alpha = ImageDraw.Draw(alpha)
    draw_alpha.text((x+20, y+20), text, fill='white', font=font)
    alpha.save('alpha.png')


    # Load the image
    img = Image.open("alpha.png")

    # Apply multiple box blur filters with decreasing radii to the original image
    for radius in [10, 5]:
        blurred_img = img.filter(ImageFilter.BoxBlur(radius=radius))
        blend_factor = 1.0 - radius / 50.0
        img = Image.blend(img, blurred_img, blend_factor)

    # Invert the original image to create the outward blur effect
    inverted_img = ImageOps.invert(img)

    # Apply multiple box blur filters with increasing radii to the inverted blurred image
    for radius in [5, 10]:
        blurred_img = inverted_img.filter(ImageFilter.BoxBlur(radius=radius))
        blend_factor = radius / 50.0
        inverted_img = Image.blend(inverted_img, blurred_img, blend_factor)

    # Invert the image again to create the final result
    final_img = ImageOps.invert(inverted_img)

    # Save the result as a new PNG image
    final_img.save("blurred_image.png")

    #



    img1 = np.zeros((1080, 1920, 3), dtype=np.uint8)
    img2 = cv2.resize(cv2.imread(image_url), (1920, 1080))

    # Load mask image
    mask_img = cv2.imread('blurred_image.png')
    mask = cv2.resize(mask_img, (img1.shape[1], img1.shape[0]))
    mask = mask.astype(float) / 255.0

    # Generate output by linear blending
    final = np.uint8(img1 * mask + img2 * (1.0 - mask))
    cv2.imwrite('black_screen.jpg', final)

def doubleshadow(text1="hello",text2="goodbye",fontsize=200,image_url="image.jpg"):
    # Some input images


    image = Image.open('gradient2.png').resize((1920, 1080))

    # Create the font and text to draw
    font = ImageFont.truetype('uni-sans.heavy-caps.otf', fontsize)

    # add alpha
    alpha = Image.new('L', (1920, 1080))
    draw = ImageDraw.Draw(alpha)


    #text 1
    x1 = 20
    y1 = image.size[1] - 200 - 190
    #text 2
    x2 = 20
    y2 = image.size[1]  - 190

    # Add the first line of text to the image
    draw.text((x1, y1), text1, font=font, fill=("pink"))

    # Add the second line of text to the image
    draw.text((x2, y2), text2, font=font, fill=("pink"))

    alpha.save('alpha.png')


    # Load the image
    img = Image.open("alpha.png")

    # Apply multiple box blur filters with decreasing radii to the original image
    for radius in [10, 5]:
        blurred_img = img.filter(ImageFilter.BoxBlur(radius=radius))
        blend_factor = 1.0 - radius / 50.0
        img = Image.blend(img, blurred_img, blend_factor)

    # Invert the original image to create the outward blur effect
    inverted_img = ImageOps.invert(img)

    # Apply multiple box blur filters with increasing radii to the inverted blurred image
    for radius in [5, 10]:
        blurred_img = inverted_img.filter(ImageFilter.BoxBlur(radius=radius))
        blend_factor = radius / 50.0
        inverted_img = Image.blend(inverted_img, blurred_img, blend_factor)

    # Invert the image again to create the final result
    final_img = ImageOps.invert(inverted_img)

    # Save the result as a new PNG image
    final_img.save("blurred_image.png")

    #



    img1 = np.zeros((1080, 1920, 3), dtype=np.uint8)
    img2 = cv2.resize(cv2.imread(image_url), (1920, 1080))

    # Load mask image
    mask_img = cv2.imread('blurred_image.png')
    mask = cv2.resize(mask_img, (img1.shape[1], img1.shape[0]))
    mask = mask.astype(float) / 255.0

    # Generate output by linear blending
    final = np.uint8(img1 * mask + img2 * (1.0 - mask))
    cv2.imwrite('black_screen.jpg', final)

# shadow()
# # Outputs
# cv2.imshow('img1', img1)
# cv2.imshow('img2', img2)
# cv2.imshow('mask', mask)
# cv2.imshow('final', final)
# cv2.waitKey(0)
# cv2.destroyAllWindows()