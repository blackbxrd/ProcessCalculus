import random
import hashlib


phrase = "0678e4bde9816012477bc96e70cc7e5b419b206af07279ff88a564d8744a54ffb5c8092df53ae75c5d8a0445e85bf9bccb927bd34b2f373a90948e2c7d856808"
max_length = 16
symbols_en = "abcdefghijklmnopqrstuvwxyz1234567890"
symbols_ru = "абвгдеёжзийклмнопрстуфхцчьыъэюя1234567890"
symbols_special = "!@#$%^&*()_+~№;:? "
file_in = open("./incorrect.txt", "w")
file_cor = open("./correct.txt", "w")


def generate_random(symbols,length):
    r = ''.join(random.choice(symbols) for i in range(length))
    return r

  
      
            
         

def check(r):
    d = hashlib.new('sha512')
    d.update(r.encode())
    f = d.hexdigest()
    incorrect = '[-] ' + r + '\t' + f
    print(incorrect)
    if f == phrase:
        correct = '\n[*] ' + r + "\t" + f
        print(correct)
        file_cor.write(correct)
        file_cor.write("\n")

for length_word in range(1, max_length+1):
    r = ''
    if length_word >= 5:
        for try_num in range(10 ** len(symbols_en)):
            r = generate_random(symbols_en, length=length_word)
            check(r)
    else:
        for i in range(len(symbols_en)):
            r += symbols_en[i] * length_word
            check(r)
            
r = generate_random(symbols_en, length=length_word)