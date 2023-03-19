#!/usr/bin/env python
from PIL import Image, ImageDraw, ImageFont


def add_subtitle(
    bg,
    text="nice",
    xy=("center", "center"),
    font="uni-sans.heavy-caps.otf",
    font_size=200,
    font_color=(255, 255, 255),
    stroke=6,
    stroke_color=(0, 0, 0),
    shadow=(20, 20),
    shadow_color=(0, 0, 200),
):

    bg = bg.resize((1920, 1080), resample=Image.NEAREST)
    stroke_width = stroke
    xy = list(xy)
    W, H = bg.width, bg.height

    # Modify font size

    font = ImageFont.truetype(str(font), font_size)

    w, h = font.getsize(text, stroke_width=stroke_width)
    if xy[0] == "center":
        xy[0] = (W - w) // 2
    if xy[1] == "center":
        xy[1] = (H - h) // 2
    draw = ImageDraw.Draw(bg)
    # if shadow:
    #     print("shadow")
    #     draw.text(
    #         (xy[0] + shadow[0], xy[1] + shadow[1]), text, font=font, fill=shadow_color
    #     )
    draw.text(
        (xy[0], xy[1]),
        text,
        font=font,
        fill=font_color,
        stroke_width=stroke_width,
        stroke_fill=stroke_color,
    )
    return bg


# from PIL import Image, ImageDraw, ImageFilter, ImageFont
#
# # Open the image
# img = Image.open("image.jpg")
#
# # Create a new ImageDraw object
# draw = ImageDraw.Draw(img)
#
# # Set the font and text to be drawn
# font = ImageFont.truetype("arial.ttf", 50)
# text = "Hello, world!"
#
# # Set the position of the text
# x, y = 50, 50
#
# # Draw the text with a black drop-down shadow
# draw.text((x+10, y+10), text, font=font, fill=(0,0,0), align="center")
#
# # Apply a Gaussian blur filter to the shadow
# shadow = draw.text((x+10, y+10), text, font=font, fill=(0,0,0), align="center")
# shadow = shadow.filter(ImageFilter.GaussianBlur(radius=10))
#
# # Paste the shadow onto the original image with an alpha channel
# img.alpha_composite(shadow, dest=(x+10, y+10))
#
# # Save the resulting image
# img.save("result.jpg")

# from PIL import Image, ImageDraw, ImageFilter, ImageFont
#
# # Open the image
# img = Image.open("image.jpg")
#
# # Create a new ImageDraw object
# draw = ImageDraw.Draw(img)
#
# # Set the font and text to be drawn
# font = ImageFont.truetype("arial.ttf", 50)
# text = "Hello, world!"
#
# # Set the position of the text
# x, y = 50, 50
#
# # Draw the text with a black drop-down shadow
# shadow = Image.new('RGBA', img.size, (0, 0, 0, 0))
# shadow_draw = ImageDraw.Draw(shadow)
# shadow_draw.text((x+10, y+10), text, font=font, fill=(0,0,0, 200), align="center")
#
# # Apply a Gaussian blur filter to the shadow
# shadow = shadow.filter(ImageFilter.GaussianBlur(radius=10))
#
# # Paste the shadow onto the original image with an alpha channel
# img.alpha_composite(shadow, dest=(x+10, y+10))
#
# # Draw the text on top of the shadow
# draw.text((x, y), text, font=font, fill=(255,255,255), align="center")
#
# # Save the resulting image
# img.save("result.jpg")

# from PIL import Image, ImageDraw, ImageFilter, ImageFont
#
# # Open the image and convert it to RGBA mode
# img = Image.open("image.jpg").convert("RGBA")
#
# # Create a new ImageDraw object
# draw = ImageDraw.Draw(img)
#
# # Set the font and text to be drawn
# font = ImageFont.truetype("arial.ttf", 50)
# text = "Hello, world!"
#
# # Set the position of the text
# x, y = 50, 50
#
# # Draw the text with a black drop-down shadow
# shadow = Image.new('RGBA', img.size, (0, 0, 0, 0))
# shadow_draw = ImageDraw.Draw(shadow)
# shadow_draw.text((x+10, y+10), text, font=font, fill=(0,0,0, 150), align="center")
#
# # Apply a Gaussian blur filter to the shadow
# shadow = shadow.filter(ImageFilter.GaussianBlur(radius=20))
#
# # Paste the shadow onto the original image with an alpha channel
# img.alpha_composite(shadow, dest=(x+10, y+10))
#
# # Draw the text on top of the shadow
# draw.text((x, y), text, font=font, fill=(255,255,255), align="center")
#
# # Save the resulting image
# img.save("result.png")
#
# from PIL import Image, ImageDraw, ImageFilter, ImageFont
#
# # Open the image and convert it to RGBA mode
# img = Image.open("image.jpg").convert("RGBA")
#
# # Create a new ImageDraw object
# draw = ImageDraw.Draw(img)
#
# # Set the font and text to be drawn
# font = ImageFont.truetype("arial.ttf", 50)
# text = "Hello, world!"
#
# # Set the position of the text
# x, y = 50, 50
#
# # Draw the text with a black drop-down shadow
# shadow = Image.new('RGBA', img.size, (0, 0, 0, 0))
# shadow_draw = ImageDraw.Draw(shadow)
# shadow_draw.text((x+10, y+10), text, font=font, fill=(0,0,0, 200), align="center")
# shadow.save("result.png")
# # Apply a Gaussian blur filter to the shadow
# shadow = shadow.filter(ImageFilter.GaussianBlur(radius=30))
#
# # Paste the shadow onto the original image with an alpha channel
# img.alpha_composite(shadow, dest=(x+10, y+10))
#
# # Draw the text on top of the shadow
# draw.text((x, y), text, font=font, fill=(255,255,255), align="center")
#
# # Convert the image to RGB mode and save it as a JPEG file
# # img.convert("RGB").save("result.jpg", "JPEG")

#!/usr/bin/env python3
# See also: https://legacy.imagemagick.org/Usage/fonts/#soft_shadow
# from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
#
# # Open background image and work out centre
# bg = Image.open('image.jpg').convert('RGB')
# x = bg.width//2
# y = bg.height//2
#
# # The text we want to add
# text = "StackOverflow"
#
# # Create font
# font = ImageFont.truetype('arial.ttf', 60)
#
# # Create piece of canvas to draw text on and blur
# blurred = Image.new('RGBA', bg.size)
# draw = ImageDraw.Draw(blurred)
# draw.text(xy=(x,y), text=text, fill='white', font=font, anchor='mm')
# blurred = blurred.filter(ImageFilter.BoxBlur(10))
#
# # Paste soft text onto background
# bg.paste(blurred,blurred)
#
# # Draw on sharp text
# draw = ImageDraw.Draw(bg)
# draw.text(xy=(x,y), text=text, fill='navy', font=font, anchor='mm')
# bg.save('result.png')

# from PIL import Image, ImageFilter, ImageOps
#
# # Load the image
# img = Image.open("alpha.png")
#
# # Blur the image with a box blur filter
# blurred_img = img.filter(ImageFilter.BoxBlur(radius=10))
#
# # Invert the blurred image to create the outward blur effect
# inverted_img = ImageOps.invert(blurred_img)
#
# # Save the result as a new PNG image
# inverted_img.save("blurred_image.png")





# from PIL import Image, ImageFilter, ImageOps
#
# # Load the image
# img = Image.open("alpha.png")
#
# # Apply multiple box blur filters with decreasing radii
# for radius in [30, 20, 10]:
#     blurred_img = img.filter(ImageFilter.BoxBlur(radius=radius))
#     img = Image.blend(img, blurred_img, 0.5)
#
# # Invert the blurred image to create the outward blur effect
# inverted_img = ImageOps.invert(img)
#
# # Save the result as a new PNG image
# inverted_img.save("blurred_image.png")


# from PIL import Image, ImageFilter, ImageOps
#
# # Load the image
# img = Image.open("alpha.png")
#
# # Apply multiple box blur filters with decreasing radii
# for radius in [30, 20, 10]:
#     blurred_img = img.filter(ImageFilter.BoxBlur(radius=radius))
#     blend_factor = 1.0 - radius / 50.0
#     img = Image.blend(img, blurred_img, blend_factor)
#
# # Invert the blurred image to create the outward blur effect
# inverted_img = ImageOps.invert(img)
#
# # Save the result as a new PNG image
# inverted_img.save("blurred_image.png")



#
# from PIL import Image, ImageFilter, ImageOps
#
# # Load the image
# img = Image.open("alpha.png")
#
# # Apply multiple box blur filters with decreasing radii to the original image
# for radius in [30, 20, 10]:
#     blurred_img = img.filter(ImageFilter.BoxBlur(radius=radius))
#     blend_factor = 1.0 - radius / 50.0
#     img = Image.blend(img, blurred_img, blend_factor)
#
# # Invert the original image to create the outward blur effect
# inverted_img = ImageOps.invert(img)
#
# # Apply multiple box blur filters with increasing radii to the inverted blurred image
# for radius in [10, 20, 30]:
#     blurred_img = inverted_img.filter(ImageFilter.BoxBlur(radius=radius))
#     blend_factor = radius / 50.0
#     inverted_img = Image.blend(inverted_img, blurred_img, blend_factor)
#
# # Invert the image again to create the final result
# final_img = ImageOps.invert(inverted_img)
#
# # Save the result as a new PNG image
# final_img.save("blurred_image.png")




# from PIL import Image, ImageFilter, ImageOps
#
# # Load the image
# img = Image.open("alpha.png")
#
# # Apply multiple box blur filters with decreasing radii to the original image
# for radius in [20, 10]:
#     blurred_img = img.filter(ImageFilter.BoxBlur(radius=radius))
#     blend_factor = 1.0 - radius / 30.0
#     img = Image.blend(img, blurred_img, blend_factor)
#
# # Invert the original image to create the outward blur effect
# inverted_img = ImageOps.invert(img)
#
# # Apply multiple box blur filters with increasing radii to the inverted blurred image
# # for radius in [10, 20, 30]:
# #     blurred_img = inverted_img.filter(ImageFilter.BoxBlur(radius=radius))
# #     blend_factor = radius / 50.0
# #     inverted_img = Image.blend(inverted_img, blurred_img, blend_factor)
#
# # Invert the image again to create the final result
# final_img = ImageOps.invert(inverted_img)
#
# # Save the result as a new PNG image
# final_img.save("blurred_image.png")