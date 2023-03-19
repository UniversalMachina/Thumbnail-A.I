# from PIL import Image, ImageChops
#
# # Open the first image to be lightened
# img1 = Image.open('image1.jpg')
#
# # Open the second image to be used as a mask
# img2 = Image.open('image2.jpg')
#
# # Resize the mask image to match the size of the first image
# img2 = img2.resize(img1.size)
#
# # Lighten the first image with the second image using the ImageChops module
# lightened = ImageChops.lighter(img1, img2)
#
# # Save the lightened image to a file
# lightened.save('lightened.jpg')





def dust(image_path="dust.jpg",  opacity=0.7):
    from PIL import Image, ImageChops
    from PIL import Image

    img = Image.open(image_path)
    black = Image.new('RGB', img.size, (0, 0, 0))
    # Blend the two images with the given opacity
    img_reduced_opacity = Image.blend(img, black, opacity)

    # Open the first image to be lightened
    img1 = Image.open('image.jpg')

    img2 = img_reduced_opacity.resize(img1.size)
    lightened = ImageChops.lighter(img1, img2)
    lightened.save('with_dust.jpg')


def smoke(image_path="with_dust.jpg",  opacity=0.7):
    from PIL import Image, ImageChops
    from PIL import Image
    # Open the image to be reduced in opacity
    img = Image.open(image_path)

    black = Image.new('RGB', img.size, (0, 0, 0))
    img_reduced_opacity = Image.blend(img, black, opacity)
    img1 = Image.open('smoke.jpg')

    img2 = img_reduced_opacity.resize(img1.size)

    lightened = ImageChops.lighter(img1, img2)

    lightened.save('with_smoke.jpg')

def light(image_path="with_smoke.jpg", output_path="test.jpg", opacity=0.7):
    from PIL import Image, ImageChops
    from PIL import Image
    # Open the image to be reduced in opacity
    img = Image.open(image_path)
    black = Image.new('RGB', img.size, (0, 0, 0))
    img_reduced_opacity = Image.blend(img, black, opacity)
    img_reduced_opacity.save(output_path)
    import cv2
    # Load the image and overlay image
    output_size = (1920, 1080)
    img = cv2.imread("image.jpg")
    overlay = cv2.imread('light.jpg')

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
    filename="finished.jpg"

    # # Write the output image to a file
    # i = 0
    # import os
    # filename = f'photos\\export\Finished.jpg'
    # while os.path.exists(filename):
    #     i += 1
    #     filename = f'photos\\export\({i}).jpg'  # Rename the file with a number if it already exists

    # Write the string to the file

    cv2.imwrite(filename, output)


def saturation(image_path="image.jpg", output_path="", opacity=0.7):
    from PIL import Image, ImageChops
    from PIL import Image, ImageEnhance
    # Open the image to be reduced in opacity
    img = Image.open(image_path)

    # Create a white image of the same size as the original image
    black = Image.new('RGB', img.size, (0, 0, 0))

    # Blend the two images with the given opacity
    img = Image.open('bus.png')
    converter = ImageEnhance.Color(img)
    img2 = converter.enhance(0.5)

    # Save the lightened image to a file
    img2.save('saturation.jpg')

def temp(image_path="image.jpg", output_path="", opacity=0.7):
    from PIL import Image, ImageEnhance

    # Open the image file
    image = Image.open("image.jpg")

    # Create an image enhancer object
    enhancer = ImageEnhance.Color(image)

    # Increase the temperature by a factor of 1.5
    temperature = 1.2
    output_image = enhancer.enhance(temperature)

    # Save the output image
    output_image.save("output_image.jpg")

def bottom_left():
    from PIL import Image, ImageDraw, ImageFont

    # Load the image
    image = Image.open("image.jpg")

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Set the font and font size
    font = ImageFont.truetype("uni-sans.heavy-caps.otf", 200)

    # Set the text to be added
    text = "Your Text Here"

    # Calculate the text size
    text_size = draw.textsize(text, font=font)

    # Set the text position
    x = 0
    y = image.size[1] - text_size[1]

    # Add the text to the image
    draw.text((x, y), text, font=font, fill=(255, 255, 255, 255))

    # Save the image
    image.save("new_image.jpg")

def bottom_left_two_lines():
    from PIL import Image, ImageDraw, ImageFont

    # Load the image
    image = Image.open("image.jpg")

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Set the font and font size
    font = ImageFont.truetype("uni-sans.heavy-caps.otf", 200)

    # Set the text to be added
    text = "Your Text Here"

    # Calculate the text size
    text_size = draw.textsize(text, font=font)

    # Set the text position
    x = 0
    y = image.size[1] - text_size[1]

    # Add the text to the image
    draw.text((x, y), text, font=font, fill=(255, 255, 255, 255))

    second_font = ImageFont.truetype("uni-sans.heavy-caps.otf", 200)

    # Set the second line of text
    second_text = "Your second text here"

    # Calculate the size of the second line of text
    second_text_size = draw.textsize(second_text, font=second_font)

    # Set the position of the second line of text
    second_x = 0
    second_y = image.size[1] - text_size[1] - second_text_size[1]

    # Add the second line of text to the image in yellow color
    draw.text((second_x, second_y), second_text, font=second_font, fill=(255, 255, 0, 255))
    # Save the image
    image.save("new_image.jpg")

# temp()
# # reduce_opacity()
# light()
#
bottom_left()
bottom_left_two_lines()