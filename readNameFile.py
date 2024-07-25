import os

# Шлях до папки
folder_path = 'picture1'

# Отримання списку файлів у папці
files = os.listdir(folder_path)

# Фільтрування списку, щоб залишити тільки файли (виключаючи папки)
file_names = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

# Виведення назв файлів
for file_name in file_names:
    print(file_name)