import string
import random

#password_generation
all_chars=string.ascii_letters + string.digits + string.punctuation
def password_generator(num=20):
    password_pool=random.choices(all_chars,k=num)
    return "".join(password_pool)

#password_generation using the predefined words
def password_generator2(random_case):
    password=[]
    spl_char=string.punctuation+string.digits
    for word in random_case:
        password.append(word)
        spl=random.choices(spl_char,k=3)
        password.append("".join(spl))
    return "".join(password)
def passphrase(words):
    random_case=[]
    for word in words:
        new_word=[]
        for char in word:
            new_letter=random.choice([char.upper(),char.lower()])
            new_word.append(new_letter)
        random_case.append("".join(new_word))
    return password_generator2(random_case)