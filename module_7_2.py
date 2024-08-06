def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}
    position_string, position_byte = 1, 0
    for i in strings:
        file.write(i + '\n')
        strings_positions[position_string, position_byte] = i
        position_string += 1
        position_byte = file.tell()
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
