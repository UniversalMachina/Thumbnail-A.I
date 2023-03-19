from PIL import Image, ImageDraw, ImageFont

def add_text_to_image(text1="Better Than", text2="You Realize", font_path='uni-sans.heavy-caps.otf', font_size=200):
    # Load the image
    stroke=6
    stroke_color=(0, 0, 0)
    stroke_width = stroke
    image = Image.open("black_screen.jpg")
    # image = Image.open("black_screen.jpg")
    # Resize the image to 1920x1080
    image = image.resize((1920, 1080))

    # Create a new image with transparent background
    text_image = Image.new("RGBA", image.size, (255, 255, 255, 0))

    # Get a drawing context
    draw = ImageDraw.Draw(text_image)

    # Set the font size and type
    font = ImageFont.truetype(font_path, font_size)

    # Get the size of the first line of text ("Better than")
    text_size1 = draw.textsize(text1, font=font)

    # Get the size of the second line of text ("you realize")
    text_size2 = draw.textsize(text2, font=font)

    # Calculate the coordinates of the center of the image
    # center_x = image.width // 2
    # center_y = image.height // 2
    center_x = image.width // 2
    center_y = image.height // 2


    # Calculate the coordinates of the top-left corner of the first line of text
    x1 = 30
    y1 = image.size[1] - 200 - 200
    # x1 = center_x - text_size1[0] // 2
    # y1 = center_y - text_size1[1] - 20


    # Calculate the coordinates of the top-left corner of the second line of text
    x2 = 30
    y2 = image.size[1]  - 200
    # x2 = center_x - text_size2[0] // 2
    # y2 = center_y + 20


    # Add the first line of text to the image
    draw.text((x1, y1), text1, font=font, fill="yellow",
        stroke_width=stroke_width,
        stroke_fill=stroke_color)

    # Add the second line of text to the image
    draw.text((x2, y2), text2, font=font, fill=(255, 255, 255, 255),
        stroke_width=stroke_width,
        stroke_fill=stroke_color)

    # Merge the text image with the original image using the alpha channel of the text image
    result = Image.alpha_composite(image.convert("RGBA"), text_image)

    # Save the result
    result.save("With_Text.png")


def add_text_overlay(text1="Better Than", text2="You Realize",fontsize=200):
    # Load the background image and resize it to 1920x1080

    gradient = Image.open('gradient2.png').resize((1920, 1080))

    # Create the font and text to draw
    font = ImageFont.truetype('uni-sans.heavy-caps.otf', fontsize)
    draw = ImageDraw.Draw(gradient)


    font_path = 'uni-sans.heavy-caps.otf'
    font_size = 200

    #add alpha
    alpha = Image.new('L', (1920, 1080))
    draw_alpha = ImageDraw.Draw(alpha)

    #add text


    # Get a drawing context
    draw = ImageDraw.Draw(alpha)

    # Set the font size and type
    font = ImageFont.truetype(font_path, font_size)

    # Get the size of the first line of text ("Better than")
    text_size1 = draw.textsize(text1, font=font)

    # Get the size of the second line of text ("you realize")
    text_size2 = draw.textsize(text2, font=font)

    # Calculate the coordinates of the center of the image
    center_x = alpha.width // 2
    center_y = alpha.height // 2

    # Calculate the coordinates of the top-left corner of the first line of text
    x1 = center_x - text_size1[0] // 2
    y1 = center_y - text_size1[1] - 20

    # Calculate the coordinates of the top-left corner of the second line of text
    x2 = center_x - text_size2[0] // 2
    y2 = center_y + 20

    # Add the first line of text to the image
    draw.text((x1, y1), text1, font=font, fill='white')

    # Add the second line of text to the image
    draw.text((x2, y2), text2, font=font, fill='white')

    alpha.save('alpha.png')


    gradient.putalpha(alpha)
    gradient.save("Text_Gradient.png")


    # Open the result image and paste it on top of the background image
    background_image = Image.open("With_Text.png")
    foreground_image = Image.open("Text_Gradient.png")
    x_offset = 0
    y_offset = 0
    background_image.paste(foreground_image, (x_offset, y_offset), foreground_image)

    # Save the resulting image
    background_image.save("With_Gradient.png")

