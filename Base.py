
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
    from ScriptWriter.TextGenerator import generate_text as tg


    non_empty_lines = [line for line in text.split("\n") if line.strip() != ""]
    string_without_empty_lines = "\n".join(non_empty_lines)
    text = string_without_empty_lines
    print(text)
    prompt=f"Given this sentence get an interesting google image search term that is one word, if there is a subject in that sentence return that. The subject must be a proper noun. Do not add punctuation. Only return the search term in the response:\n{topic}\nHere are examples of inputs and outputs for this prompt\nInput: Analyzing the narrative structure of Mass Effect\nOutput: Mass Effect\nInput: Analyzing the narrative structure of Final Fantasy\nOutput: Final Fantasy"
    search=tg(prompt)
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

# from ScriptWriter import TextGenerator as tg
# topic="Mass Effect"
# thumb_ex=tg.thumbnail_phrases
# prompt=f"generate text on this topic {topic} that's no more than 28 characters not including spaces and that has no words with more than 14 characters\n ideally the amount of characters should be between 7 and 24\nMake it sound like this:\n{thumb_ex}"
# text=tg.generate_outline(prompt)
# print(text)
# thumbnail(topic,text)