# Напишите программу, удаляющую из текста все слова, содержащие ""абв""
    
str_s = 'Съешьабв же ещёабв абвэтих мягких абвфранцузских булок абвда выпей чаюабв'
split_string = str_s.split()

# filter and lambda
print(*(filter(lambda x: not 'абв' in x, split_string)))

# map and lambda
print(*(map(lambda item: '' if 'абв' in item else item, split_string)))

# list comprehension
print(*[item for item in split_string if not 'абв' in item])