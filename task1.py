# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

import os
os.system('cls')

text = 'коли лоАБВс тира ыадАБВлада ововов АБВлада дадвАБВжы'
print('Первоначальный текст:')
print(text)
text = list(filter(lambda el: 'абв' not in el.lower(), text.split()))
print('Текст без АБВ:')
print(' '.join(text))