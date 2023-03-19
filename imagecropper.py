from PIL import Image

def resize_and_crop_image(image_path,export_path):
    # Open the image file
    # Open the image file

    from PIL import Image



    # Open the image file
    img = Image.open(image_path)

    # Get the current width and height of the image
    width, height = img.size

    # Calculate the new dimensions that maintain the aspect ratio of the image
    if width/1920 < height/1080:
        # Scale based on the width
        new_width = 1920
        new_height = int((new_width / width) * height)
    else:
        # Scale based on the height
        new_height = 1080
        new_width = int((new_height / height) * width)

    # Resize the image
    img = img.resize((new_width, new_height))

    # # Save the resized image
    # img.save(export_path)
    #
    # from PIL import Image
    #
    # # Open the image file
    # img = Image.open('resized_example.jpg')

    cropped_img = img.crop((0, 0, 1920, 1080))
    # Resize the cropped image to exactly 1920 by 1080

    # Save the cropped and resized image
    cropped_img.save(export_path)




import cv2
import numpy as np
def dust(image_url="",opacity=0.6):
    from PIL import Image, ImageChops

    # Open the first image, resize it and convert to RGBA mode
    img1 = Image.open(image_url).resize((1920, 1080)).convert('RGBA')

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
    return output



def color_dodge_blend():
    # Load the image and overlay image
    print("dust")
    dust()
    print("smoke")
    smoke()
    output=light()


    # Write the output image to a file
    i = 0
    import os
    filename = f'photos\\export\Finished.jpg'
    while os.path.exists(filename):
        i += 1
        filename = f'photos\\export\({i}).jpg'  # Rename the file with a number if it already exists

    # Write the string to the file

    cv2.imwrite(filename, output)
def filter(image_path):
    # Open the image file
    # Open the image file

    from PIL import Image

    dust(image_path)
    smoke()
    output=light()
    # Open the image file


    cv2.imwrite(image_path, output)


