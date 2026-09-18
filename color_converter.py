from PIL import Image, ImageDraw

def letter_darkness_convert(img):
    new_img = img
    imgWidth, imgHeight = new_img.size
    for y in range(imgHeight):
        for x in range(imgWidth):
            colorR, colorG, colorB = new_img.getpixel((x, y))
            f = int(round(0.299 * colorR + 0.587 * colorG + 0.114 * colorB))
            new_img.putpixel((x, y), (f, f, f))
    return new_img

def letter_black_white_style(img):
    new_img = img
    imgWidth, imgHeight = new_img.size
    for y in range(imgHeight):
        for x in range(imgWidth):
            fCount = new_img.getpixel((x, y))[0]
            if fCount >= 0.8 * 255:
                new_img.putpixel((x, y), (255, 255, 255))
            else:
                new_img.putpixel((x, y), (0, 0, 0))                
    return new_img

def simplication_letter(img):
    imgX, imgY = img.size
    final_letter = Image.new("RGB", (imgX // 2, imgY // 2), (255, 255, 255))
    for y in range(0, imgY, 2):
        for x in range(0, imgX, 2):
            if y < imgY - 1 and x < imgX - 1:
                colorsForSimple = (img.getpixel((x, y)),
                                   img.getpixel((x + 1, y)),
                                   img.getpixel((x, y + 1)),
                                   img.getpixel((x + 1, y + 1)))
                countWhite = 0
                countBlack = 0
                for l in colorsForSimple:
                    if l == (255, 255, 255):
                        countWhite += 1
                    elif l == (0, 0, 0):
                        countBlack += 1
                if countBlack >= 2:
                    final_letter.putpixel((x // 2, y // 2), (0, 0, 0))
                else:
                    final_letter.putpixel((x // 2, y // 2), (255, 255, 255))
    return final_letter

letter_example = Image.open("letter_imgs/Letter1.png").convert("RGB")

if __name__ == "__main__":
    letter_darkness_var = letter_darkness_convert(letter_example)
    
    letter_black_white = letter_black_white_style(letter_darkness_var)
    letterX, letterY = letter_black_white.size

    while letterY > 32 and letterX > 32:
        letter_black_white = simplication_letter(letter_black_white)
        letterX, letterY = letter_black_white.size
    
    letter_black_white.save("darkness_letter/Letter1.png")
