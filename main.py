import cv2
from pytesseract import pytesseract


path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def remove_noise(image):
    return cv2.medianBlur(image, 5)

def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)[1]

def main():
    image = cv2.imread('image.jpg')

    #no_noise = remove_noise(image)
    gray = get_grayscale(image)
    thresh = thresholding(gray)

    cv2.imwrite('result_image.jpg', thresh)

    file = open("text_output.txt", "a")

    text = pytesseract.image_to_string('result_image.jpg')

    print(text)

if __name__ == '__main__':
    main()
