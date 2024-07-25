import cv2
import pytesseract
from imutils import contours
pytesseract.pytesseract.tesseract_cmd ='C:/Users/Windows10/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
image = cv2.imread("picture/ex6.jpg")
height, width, _ = image.shape
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # преобразовать изображение в черно-белое
cv2.imshow("Gray Image", image_gray) #вывести на экран для проверки
cv2.waitKey()
threshold = cv2.threshold(image_gray, 0, 255, cv2.THRESH_OTSU)[1] # пороговая обработка для выделения контуров
cv2.imshow("Threshold", threshold) #вывести на экран для проверки
cv2.waitKey()
contourss = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #Найдем все контуры
contourss, _ = contours.sort_contours(contourss[0]) # отсортируем их
chars = set('0123456789,') # создадим множество цифр для отсечения "мусорных" текстов
for c in contourss: # переберем все контуры
 area = cv2.contourArea(c) # найдем площадь контура
 x, y, w, h = cv2.boundingRect(c)
 if area > 5000: # если площадь соизмерима с номером
    img = image[y:y+h, x:x+w] # получим этот контур из исходного изображения
    result = pytesseract.image_to_string(img, lang='rus+eng') # преобразуем его в текст
    if not (' ' in result) and len(result) > 7 and any((c in chars) for c in result):
 # отсекая "мусорные" варианты, выведем распознанный номер в консоль
        while '\n' in result:
            result = ('\n'.join(result.split('\n')[:-1])) # избавимся отлишних переносов строки
        print(result)
cv2.waitKey()