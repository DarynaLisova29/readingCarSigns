import cv2
import pytesseract
from imutils import contours
from readNameFile import *

def extract_text_from_image(image_path, min_area=5000):

    pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR/tesseract.exe'

    image = cv2.imread(image_path)
    height, width, _ = image.shape
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts, _ = contours.sort_contours(cnts[0])

    results = []
    for c in cnts:
        area = cv2.contourArea(c)
        x, y, w, h = cv2.boundingRect(c)
        if area > min_area:
            img = image[y:y + h, x:x + w]
            result = pytesseract.image_to_string(img, lang="rus+eng")
            if len(result) > 7:
                results.append(result)

    if len(results) == 1:
        return results[0]
    else:
        return results

folder_path = 'picture1'
file_list = get_file_list(folder_path)
i=1;
for file_name in file_list:
    file=folder_path+"/"+file_name
    # print(i)
    print(i, extract_text_from_image(file))
    i=i+1
