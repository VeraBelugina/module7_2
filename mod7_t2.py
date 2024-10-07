def custom_write(file_name, strings):
    strings_positions = {}
    num_string = 0
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:
        start = file.tell()
        file.write(string + '\n')
        num_string += 1
        strings_positions[(num_string, start)] = string
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
