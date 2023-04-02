
def makethumbnail(image_url,text="house"):
    def divide_string(s):
        # If the string has 14 characters or less, return it as is
        if len(s) <= 14:
            return s, ''

        # Split the string into words
        words = s.split()

        # Find the index of the middle word (rounded down if the sentence has an odd number of words)
        midpoint = len(words) // 2

        # Join the first half of the words into a string
        first = ' '.join(words[:midpoint])

        # Join the second half of the words into a string
        second = ' '.join(words[midpoint:])
        return first, second
    import Text
    if len(text) <= 14:
        import greyscalemask
        greyscalemask.shadow(text,200,image_url)
        print("the shadow worked")
        from PIL import Image, ImageDraw, ImageFont
        # text="Better Than"
        bg = Image.open("black_screen.jpg")
        bg = Text.add_subtitle(bg, text=text, font_size=200)
        bg.save("With_Text.png")
        print("the text worked")
        # import Gradient
        # Gradient.add_text_overlay(text,fontsize=200)
        # print("the gradient worked")
        import Overlay
        Overlay.color_dodge_blend()
    else:

        first, second = divide_string(text)
        print(first,second)
        import greyscalemask

        greyscalemask.doubleshadow(first,second,200,image_url)
        import doubletext
        doubletext.add_text_to_image(text1=first,text2=second)

        # doubletext.add_text_overlay(text1=first,text2=second)
        import Overlay
        Overlay.color_dodge_blend()


def thumbnail(topic="Mass Effect",text="Better than You Think"):
    search=tg(topic)
    non_empty_lines = [line for line in search.split("\n") if line.strip() != ""]
    string_without_empty_lines = "\n".join(non_empty_lines)
    search = string_without_empty_lines
    print(search)
    import downloader
    downloader.main(search)
    import imagecropper
    for i in range(10):
        try:
            imagecropper.resize_and_crop_image(f'photos\images\image{i}.jpeg',f'photos\\rescaled\image{i}.jpeg')
        except:
            pass

    for i in range(10):

        imagecropper.filter(f'photos\\rescaled\image{i}.jpeg')


    for i in range(10):
        print("this is a test")
        try:

            makethumbnail(f'photos\\rescaled\image{i}.jpeg',text)
        except:
            pass


topic="Mass Effect"

text="Better than You Think"

thumbnail(topic,text)
