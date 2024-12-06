# Открываем файл text.txt в режиме чтения
with open('text.txt', 'r', encoding='utf-8') as file:
    # Читаем содержимое файла
    text = file.read()

# Разделяем текст на слова
words = text.split()

# Создаем множество для хранения уникальных слов
unique_words = set()

# Добавляем каждое слово в множество уникальных слов
for word in words:
    unique_words.add(word)

# Открываем файл output.txt в режиме записи
with open('output.txt', 'w', encoding='utf-8') as file:
    # Записываем каждое уникальное слово в новый файл
    for word in unique_words:
        file.write(word + '\n')

print("Уникальные слова успешно записаны в файл output.txt")
