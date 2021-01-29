
import string




def encode(text, key):
    
    tt = str.maketrans(dict.fromkeys(string.punctuation))
    text = text.translate(tt)
    
    index = []
    for i in range(len(text)):
        if text[i] == ' ':
            index.append(i)
    
    text = text.upper().replace(' ', '')
    
    key = key.upper()
    
    key *= len(text)//len(key)+1
    encoded_text = ''
    
    for i, j in enumerate(text):
        symbol = (ord(j) + ord(key[i]))
        encoded_text += chr(symbol % 32+1040)
   
    for i in index:
        encoded_text = encoded_text[0:i] + ' ' + encoded_text[i:]
    return encoded_text.lower()


def decode(text, key):
    tt = str.maketrans(dict.fromkeys(string.punctuation))
    text = text.translate(tt)
    index = []
    for i in range(len(text)):
        if text[i] == ' ':
            index.append(i)
    text = text.upper().replace(' ', '')
    key = key.upper()
    key *= len(text)//len(key)+1
    decoded_text = ''
    for i, j in enumerate(text):
        symbol = (ord(j) - ord(key[i]))
        decoded_text += chr(symbol % 32+1040)
    for i in index:
        decoded_text = decoded_text[0:i] + ' ' + decoded_text[i:]
    return decoded_text.lower()


print("1 - Шифрование")
print("2 - Расшифровка")
answer_1 = int(input('Ваш выбор: '))
if answer_1 == 1:
    print("1 - Создать файл")
    print("2 - Выбор файла")
    answer_2 = int(input('Ваш выбор '))
    if answer_2 == 1:
        file_text = input('Введите имя файла (с расширением): ')
        
        f = open(file_text, 'w')
        text = input('Введите текст: ')
        
        f.write(text)
        key = input('Введите ключ: ')
        
        encoded_message = encode(text, key)
        
        f = open('encoded.txt', 'w')
        
        f.write(encoded_message)
        
        f.close()
    if answer_2 == 2:
        file_text = input('Введите имя файла (с расширением): ')
        key = input('Введите ключ: ')
        f = open(file_text, 'r')
        text = f.read()
        encoded_message = encode(text, key)
        f.close()
        f = open('encoded.txt', 'w')
        f.write(encoded_message)
        f.close()
if answer_1 == 2:
    print("1 - Создать файл")
    print("2 - Выбор файла")
    answer_2 = int(input('Ваш выбор: '))
    if answer_2 == 1:
        file_text = input('Введите имя файла (с расширением): ')
        f = open(file_text, 'w')
        text = input('Введите текст: ')
        f.write(text)
        key = input('Введите ключ: ')
        decoded_message = decode(text, key)
        f = open('decoded.txt', 'w')
        f.write(decoded_message)
        f.close()
    if answer_2 == 2:
        file_text = input('Введите имя файла (с расширением): ')
        key = input('Введите ключ: ')
        f = open(file_text, 'r')
        text = f.read()
        decoded_message = decode(text, key)
        f.close()
        f = open('decoded.txt', 'w')
        f.write(decoded_message)
        f.close()
