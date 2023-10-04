# 1
def find_elements_larger_than_neighbors(arr):
    result = []
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            result.append(i)
    return result


array = (1, 3, 5, 2, 6, 8, 4)
result_indices = find_elements_larger_than_neighbors(array)
print("Порядковые номера элементов, больших своих соседей:", result_indices)


# 2
def swap_elements(matrix):
    for col in range(len(matrix[0])):
        first_neg_row = None
        last_zero_row = None

        for row in range(len(matrix)):
            if matrix[row][col] < 0 and first_neg_row is None:
                first_neg_row = row
            if matrix[row][col] == 0:
                last_zero_row = row

        if first_neg_row is not None and last_zero_row is not None:
            matrix[first_neg_row][col], matrix[last_zero_row][col] = matrix[last_zero_row][col], matrix[first_neg_row][
                col]


matrix = (
    [1, 2, -3, 4],
    [5, -6, 7, 8],
    [9, 10, 0, -11]
)

print("Было:")
for row in matrix:
    print(row)

swap_elements(matrix)

print("\nСтало:")
for row in matrix:
    print(row)


# 3
def count_unique_elements(sorted_list):
    unique_count = 0

    for i in range(len(sorted_list)):

        if i == len(sorted_list) - 1 or sorted_list[i] != sorted_list[i + 1]:
            unique_count += 1

    return unique_count


sorted_list = [1, 2, 2, 3, 3, 3, 4, 5, 5, 6]

unique_count = count_unique_elements(sorted_list)
print("Количество различных элементов:", unique_count)
# 4
print("ПРЕДУПРЕЖДЕНИЕ!")
print("не вводите слишком много школьников, долго заполнять будете")
all_languages = set()

any_language = set()

n = int(input("введите кол-во школьников: "))

for _ in range(n):
    num_languages = int(input("кол-во языков которые знает школьник: "))

    student_languages = set()

    for _ in range(num_languages):
        language = input("введите название языка: ")
        student_languages.add(language)

    if not all_languages:
        all_languages = student_languages.copy()
    else:

        all_languages = all_languages.intersection(student_languages)

    any_language = any_language.union(student_languages)


print(len(all_languages))
for language in sorted(all_languages):
    print(language)


print(len(any_language))
for language in sorted(any_language):
    print(language)
# 5
english_to_latin = {}
n = int(input("кол-во слов: "))
print("///пример:///")
print("///apple - malum, pomum///")
for _ in range(n):
    line = input().split(" - ")
    english_word = line[0]
    latin_translations = line[1].split(", ")
    english_to_latin[english_word] = latin_translations

latin_to_english = {}
for english_word, latin_translations in english_to_latin.items():
    for latin_word in latin_translations:
        if latin_word not in latin_to_english:
            latin_to_english[latin_word] = []
        latin_to_english[latin_word].append(english_word)

print(len(latin_to_english))
for latin_word in sorted(latin_to_english.keys()):
    english_words = sorted(latin_to_english[latin_word])
    print(latin_word + " - " + ", ".join(english_words))

# для примера введём:
# 4
# apple - malum, pomum, popula
# fruit - baca, bacca, popum
# punishment - malum, multa
# popula - fruit
