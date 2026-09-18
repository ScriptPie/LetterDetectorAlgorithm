from PIL import Image, ImageDraw

def most_top_point_left(image):
    imgWidth, imgHeight = image.size
    for y in range(imgHeight):
        for x in range(imgWidth):
            if image.getpixel((x, y)) == (0, 0, 0):
                return (x, y)
    return -1

def most_top_point_right(image):
    imgWidth, imgHeight = image.size
    posY = -1
    posX = -1
    for x in range(imgHeight):
        for y in range(imgWidth):
            if image.getpixel((x, y)) == (0, 0, 0):
                return (x, y)
    return -1

def most_bottom_point_left(image):
    imgWidth, imgHeight = image.size
    posY = -1
    posX = -1
    for x in range(imgHeight):
        for y in range(imgWidth - 1, -1, -1):
            if image.getpixel((x, y)) == (0, 0, 0):
                return (x, y)
    return -1

def most_bottom_point_right(image):
    imgWidth, imgHeight = image.size
    posY = -1
    posX = -1
    for y in range(imgHeight):
        for x in range(imgWidth):
            if image.getpixel((x, y)) == (0, 0, 0):
                posX, posY = x, y
    if posY == -1 or posX == -1:
        return -1
    return (posX, posY)

letter_image = Image.open("darkness_letter/Letter1.png").convert("RGB")

most_top_left = -1
most_top_right = -1
most_bottom_left = -1
most_bottom_right = -1

if __name__ == "__main__":
    most_top_left = most_top_point_left(letter_image)
    most_top_right = most_top_point_right(letter_image)
    most_bottom_left = most_bottom_point_left(letter_image)
    most_bottom_right = most_bottom_point_right(letter_image)
