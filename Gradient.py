from PIL import Image, ImageDraw, ImageFont


def add_text_overlay(text, fontsize=200):
    # Load the background image and resize it to 1920x1080
    gradient = Image.open('gradient2.png').resize((1920, 1080))

    # Create the font and text to draw
    font = ImageFont.truetype('uni-sans.heavy-caps.otf', fontsize)
    draw = ImageDraw.Draw(gradient)
    text_width, text_height = draw.textsize(text, font)
    x = (1920 - text_width) / 2
    y = (1080 - text_height) / 2

    # Create a new alpha channel
    alpha = Image.new('L', (1920, 1080))
    draw_alpha = ImageDraw.Draw(alpha)
    draw_alpha.text((x, y), text, fill='white', font=font)
    alpha.save('alpha.png')

    # Use text cutout as alpha channel for background image
    gradient.putalpha(alpha)
    gradient.save("Text_Gradient.png")
    # Open the result image and paste it on top of the background image
    background_image = Image.open("With_Text.png")
    foreground_image = Image.open("Text_Gradient.png")
    x_offset = -6
    y_offset = -6
    background_image.paste(foreground_image, (x_offset, y_offset), foreground_image)

    # Save the resulting image
    background_image.save("With_Gradient.png")