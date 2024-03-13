import cv2
from pytesseract import pytesseract

from cv2.typing import MatLike
from cv2 import UMat


path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract


class ImageHandler():
    def get_grayscale(self, image: MatLike | UMat) -> MatLike | UMat:
        """Преобразовать изображение в полутоновое"""
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def handle(self, image: MatLike | UMat) -> bool:
        """Обработать изображение"""
        image = cv2.imread(image)

        gray_image = self.get_grayscale(image)

        cv2.imwrite('result_image.jpg', gray_image)
        return gray_image

def print_text(image: MatLike | UMat) -> None:
    """Вывести текст"""
    handler = ImageHandler()
    result_image = handler.handle(image)
    text = pytesseract.image_to_string(result_image)
    print(text)