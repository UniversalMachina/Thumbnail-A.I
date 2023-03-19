import cv2
import numpy as np
def dust(opacity=0.6):
    from PIL import Image, ImageChops

    # Open the first image, resize it and convert to RGBA mode
    img1 = Image.open('With_Text.png').resize((1920, 1080)).convert('RGBA')

    # Open the second image, resize it and convert to RGBA mode
    img = Image.open("dust.jpg").resize((1920, 1080)).convert('RGBA')

    # Create a black image with the same size as img and convert to RGBA mode
    black = Image.new('RGBA', img.size, (0, 0, 0, 255))

    # Set the opacity for blending

    # Blend the two images with the given opacity
    img2 = Image.blend(img, black, opacity)

    # Lighten the two images
    lightened = ImageChops.lighter(img1, img2)

    # Save the result
    lightened.save('with_dust.png')


def smoke(opacity=0.6):
    from PIL import Image, ImageChops
    from PIL import Image
    # Open the image to be reduced in opacity
    # Open the first image, resize it and convert to RGBA mode
    img1 = Image.open('with_dust.png').resize((1920, 1080)).convert('RGBA')

    # Open the second image, resize it and convert to RGBA mode
    img = Image.open("smoke.jpg").resize((1920, 1080)).convert('RGBA')

    # Create a black image with the same size as img and convert to RGBA mode
    black = Image.new('RGBA', img.size, (0, 0, 0, 255))

    # Set the opacity for blending

    # Blend the two images with the given opacity
    img2 = Image.blend(img, black, opacity)

    # Lighten the two images
    lightened = ImageChops.lighter(img1, img2)

    # Save the result
    lightened.save('with_smoke.png')

def light( opacity=0.3):
    from PIL import Image, ImageChops
    from PIL import Image
    # Open the image to be reduced in opacity
    img = Image.open("light.jpg").convert('RGB')
    black = Image.new('RGB', img.size, (0, 0, 0))
    img_reduced_opacity = Image.blend(img, black, opacity)
    img_reduced_opacity.save("test.png")
    import cv2
    # Load the image and overlay image
    output_size = (1920, 1080)
    img = cv2.imread("with_smoke.png")
    overlay = cv2.imread('test.png')

    # Check if the images were loaded successfully
    if img is None:
        print("Error: Could not read image file.")
        return

    if overlay is None:
        print("Error: Could not read overlay file.")
        return

    # Rescale the images
    img = cv2.resize(img, output_size)
    overlay = cv2.resize(overlay, output_size)

    # Apply the color dodge blending effect
    output = cv2.divide(img, 255 - overlay, scale=256)
    # return output
    i = 0
    import os
    filename = f'photos\\export\Finished.jpg'
    while os.path.exists(filename):
        i += 1
        filename = f'photos\\export\({i}).jpg'  # Rename the file with a number if it already exists

    # Write the string to the file

    cv2.imwrite(filename, output)


def color_dodge_blend():
    # Load the image and overlay image
    # print("dust")
    # dust()
    # print("smoke")
    # smoke()
    # output=light()

    from PIL import Image
    img1 = Image.open('With_Text.png').convert('RGB')

    # Write the output image to a file
    i = 0
    import os
    filename = f'photos\\export\Finished.jpg'
    while os.path.exists(filename):
        i += 1
        filename = f'photos\\export\({i}).jpg'  # Rename the file with a number if it already exists

    # Write the string to the file
    img1.save(filename)
    # cv2.imwrite(filename, output)


def color_dodge_blend_backup():
    # Load the image and overlay image
    dust()
    smoke()
    output_size = (1920, 1080)
    img = cv2.imread('with_smoke.jpg')
    overlay = cv2.imread('overlay.jpg')

    # Check if the images were loaded successfully
    if img is None:
        print("Error: Could not read image file.")
        return
    if overlay is None:
        print("Error: Could not read overlay file.")
        return

    # Rescale the images
    img = cv2.resize(img, output_size)
    overlay = cv2.resize(overlay, output_size)

    # Apply the color dodge blending effect
    output = cv2.divide(img, 255 - overlay, scale=256)

    # Write the output image to a file
    i = 0
    import os
    filename = f'photos\\export\Finished.jpg'
    while os.path.exists(filename):
        i += 1
        filename = f'photos\\export\({i}).jpg'  # Rename the file with a number if it already exists

    # Write the string to the file

    cv2.imwrite(filename, output)
# dust()
# smoke()
# light()