import os

def get_file_list(folder_path):
    # Отримання списку файлів і папок у вказаній директорії
    files = os.listdir(folder_path)

    # Фільтрування списку, щоб залишити тільки файли (виключаючи папки)
    file_names = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

    return file_names

# # Виклик функції та виведення результату
# folder_path = 'picture1'
# file_list = get_file_list(folder_path)
# print(file_list)