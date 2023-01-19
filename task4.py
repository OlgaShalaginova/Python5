# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

import os
os.system('cls')
import random

with open('HW5Python/text_to_RLE.txt', 'r') as file_data:
   string_pos = file_data.read()
   list_in = list(string_pos)
print(list_in)
print('Первоначальный текст:', string_pos)

count = 1
result = []
for i in range(1, len(list_in)):
   if list_in[i] == list_in[i - 1]:
      count += 1
   else:
      if count > 1:
         result.append(str(count))
         count = 1
      result.append(list_in[i - 1])
if list_in[len(list_in) - 2] == list_in[len(list_in) - 1]:
   result.append(str(count))
   result.append(list_in[len(list_in) - 2])
result_str = ''.join(result)
print('Зашифрованный текст: ', result_str)

with open('HW5Python/text_from_RLE.txt', 'w') as file_data:
     file_data.writelines(result_str)

with open('HW5Python/text_from_RLE.txt', 'r') as file_data:
   string_rle = file_data.read()
   list_rle = list(string_rle)
print(list_rle)

list_rle_return = []
now_digit = ''

for i in range(1, len(list_rle)):
   if list_rle[i].isdigit():
      continue
   elif list_rle[i - 1].isdigit():
      list_rle_return.append(int(list_rle[i - 1]) * list_rle[i])
   else:
      list_rle_return.append(list_rle[i])
print(list_rle_return)
result_rle_str = ''.join(list_rle_return)
print('Расшифрованный текст: ', result_rle_str)

with open('HW5Python/text_from_RLE_return.txt', 'w') as file_data:
   file_data.writelines(result_rle_str)