import aspose.ocr as ocr
from readNameFile import *
def algoritm(file_name):
    # Instantiate Aspose.OCR API
    api = ocr.AsposeOcr()

    # Add image to the recognition batch
    input = ocr.OcrInput(ocr.InputType.SINGLE_IMAGE)
    input.add(file_name)

    # Recognize the image
    result = api.recognize_car_plate(input)

    # Print recognition result
    # print(result[0].recognition_text)
    return result[0].recognition_text

folder_path = 'picture1'
file_list = get_file_list(folder_path)
i=0
for file_name in file_list:
    file=folder_path+"/"+file_name
    # print(i)
    # print(file_name, algoritm(file))
    print(f"{i}. Назва файла: {file_name}\n Результат: {algoritm(file)}\n")
    i=i+1
