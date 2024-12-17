with open("text.txt", 'r') as file:  # Открываем файл, выдав имя file
    text = file.read()  # Читаем строку
words = text.split()  # Делим строку на слова, записывая в список
unicum = list()  # Создаем новый список для уникальных слов
for word in words:  # Для слова в словах
    if word not in unicum:  # Если слово не в списке для уникальных слов
        unicum.append(word) # Записываем слово в список с уникальными словами
with open("output.txt", "w") as file:  # Открыв файл, даём ему имя file
    file.write("Список уникальных слов из text.txt: ")  # Записываем в файл текст
    for word in unicum:  # Для каждого слова в уникальном списке
        file.write(word + " ")  # Записать это слово в файл
