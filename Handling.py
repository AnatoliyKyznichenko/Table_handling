import re
import csv


# all regexes for phone numbers
regexes = (r"[\d]{3}-[\d]{3}-[\d]{3}", r"\+?[\d]{3}-[\d]{3}-[\d]{3}",
           r"\+?\b[\d]{3}-[\d]{3}-[\d]{3}\b", r"^[\+\(]?\d+(?:[- \)\(]+\d+)+$",
           r"^(\([0-9]{3}\) ?|[0-9]{3}-)[0-9]{3}-[0-9]{4}$",
           r"^(?:0|\+?44)\s?(?:\d\s?){9,11}$", r"^(?:(?:\+|00)33|0)\s*[\d](?:[\s.-]*\d{2}){4}$",
           r"[\+\d]?(\d{2,3}[-\.\s]??\d{2,3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})",
           r"""(
(\d{3}|\(\d{3}\))?   # Териториальный код
(\s|-|\.)?           # Разделитель
(\d{3})              # Первые 3 цифры
(\s|-|\.)?           # Разделитель
(\d{4})              # Последние 4 цифры
(\s*(ext|x|ext.)\s*(\d{2,5}))? # Добавочный номер
)""")


def contains_phone_number(string: str) -> bool:
    # search for phone number in this string using different regexes
    #поиск номера телефона в этой строке с помощью различных регексов
    for regex in regexes:
        if re.search(regex, string.replace(" ", ""), re.VERBOSE):
            return True # if there are any phone number match -> return True (если есть совпадения телефонных номеров -> возвращаем True)
    return False # else return False

# we want to see progress and result in our console
line = 0
matches = 0
filename = "message_edit.csv"


with open(filename, "r", newline="", encoding='utf8') as csvinput:
    reader = csv.reader(csvinput)

    result = list()

    # add new column name
    row = next(reader)
    row.append("with_number")

    result.append(row)

    # checking other columns for phone number(проверка других колонок на наличие номера телефона)
    for row in reader:
        # row is a list of columns in current row(row - список столбцов в текущей строке)
        line += 1 # increment line by 1 to see where we are(увеличивайте строку на 1, чтобы увидеть, где мы находимся)
        if contains_phone_number(row[2]): # if there are phone in text_message(если в text_message есть телефон)
            matches += 1
            print(line)  # what line was that(что это была за строчка)
            row.append("True") # we should write True to that row(мы должны записать True в эту строку)
        else:
            row.append("False") # we should write False if there are no phone number in this row
        result.append(row) # in the end we should add this row to result list

    # we should open file to write in the end of the program to avoid re-writing it by nothing
    #мы должны открыть файл для записи в конце программы, чтобы не переписывать его впустую
    with open(filename, "w", encoding='utf-8') as csvoutput:
        writer = csv.writer(csvoutput)
        writer.writerows(result) # and write result list to this file(и записать список результатов в этот файл)


# show result
print("matches:", matches)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/