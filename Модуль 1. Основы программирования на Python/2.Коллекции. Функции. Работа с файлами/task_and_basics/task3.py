"""
Программа считывает со стандартного потока ввода имя текстового файла. В файле содержится некоторый текст.

Напишите программу, которая будет считывать и выводить, сколько раз встречается каждое слово. Формат вывода:
 в каждой строке количество вхождений слова, затем через пробел само слово. При выводе необходимо отсортировать слова
  следующим образом: от самых частых к самым редким, среди слов с одинаковым количеством вхождений — по алфавиту,
  сначала слова, начинающиеся с заглавных букв, а затем  - со строчных.

Слово — последовательность символов, разделенных пробелами и концами строк. Если после слова следует знак препинания,
то он также относится к слову.
Примечание. Вы можете написать собственную функцию, реализующую сортировку, а можете воспользоваться функцией
Python sorted().

"""
if __name__ == "__main__":
    file_name = input()
    word_counts = {}

    with open(file_name, 'r') as file:
        content = file.read()
        content_clean = content.replace("\n", " ")
        content_full = content_clean.split()  # we get all the words
        word_dictionary = {}
        for word in content_full:
            if word in word_dictionary:
                word_dictionary[word] += 1
            else:
                word_dictionary[word] = 1
        for word, count in sorted(word_dictionary.items(), key=lambda x: (-x[1], x[0])):
            print(f'{count} {word}')

"""
The lamda function here

x takes the tuple of the key value pair from the dictionary

x[1] is the value, the negative sign makes it go to the end
x[0] is the word, so we sort it on the word, and as the sort sorts the smallest from largest 

We get the largest key and the alphabetical word in the first

"""