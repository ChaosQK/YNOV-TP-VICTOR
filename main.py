# fontion max()
def max(num1, num2):
    if num1 >= num2:
        return num1
    else:
        return num2


# fonction max_of_three
def max_of_three(num1, num2, num3):
    if num1 >= num2 and num3:
        return num1
    elif num2 >= num1 and num3:
        return num2
    else:
         return num3


# fonction len()
def len(text):
    x = 0
    for i in text:
        x += 1
    return x


def match_vowel(char):
    vowel = ["a", "e", "i", "o", "u", "y"]
    return char in vowel


def translate(text):
    translated = []
    for i in text:
        translated.append(i)
        if not match_vowel(i) and i != " ":
            translated.append("o" + i)
    return "".join(translated)


def sum(array):
    sum = 0
    for i in array:
        sum += i
    return sum


def multiply(array):
    mult = 1
    for i in array:
        mult *= i
    return mult


def reverse(text):
    rev = str()
    for i in range(len(text)-1, -1, -1):
        rev += text[i]
    return rev


def is_palindrome(palindrom):
    return palindrom == reverse(palindrom)


def is_member(arg, array):
    i = 0
    while i != len(array):
        if arg == array[i]:
            return True
        i += 1
    return False


def overlapping(array1, array2):
    for char1 in array1:
        for char2 in array2:
            if char1 == char2:
                return True
    return False


def generate_n_chars(n, c):
    string = []
    for i in range(n):
        string.append(c)
    return "".join(string)


def histogram(array):
    for num in array:
        print(generate_n_chars(num, "*"))


def max_in_list(array):
    highest = 0
    for i in array:
        for j in array:
            if highest < j:
                highest = j

# fontion max()
def max(num1, num2):
    if num1 >= num2:
        return num1
    else:
        return num2


# fonction max_of_three
def max_of_three(num1, num2, num3):
    if num1 >= num2 and num3:
        return num1
    elif num2 >= num1 and num3:
        return num2
    else:
         return num3


# fonction len()
def len(text):
    x = 0
    for i in text:
        x += 1
    return x


def match_vowel(char):
    vowel = ["a", "e", "i", "o", "u", "y"]
    return char in vowel


def translate(text):
    translated = []
    for i in text:
        translated.append(i)
        if not match_vowel(i) and i != " ":
            translated.append("o" + i)
    return "".join(translated)


def sum(array):
    sum = 0
    for i in array:
        sum += i
    return sum


def multiply(array):
    mult = 1
    for i in array:
        mult *= i
    return mult


def reverse(text):
    rev = str()
    for i in range(len(text)-1, -1, -1):
        rev += text[i]
    return rev


def is_palindrome(palindrom):
    return palindrom == reverse(palindrom)


def is_member(arg, array):
    i = 0
    while i != len(array):
        if arg == array[i]:
            return True
        i += 1
    return False


def overlapping(array1, array2):
    for char1 in array1:
        for char2 in array2:
            if char1 == char2:
                return True
    return False


def generate_n_chars(n, c):
    string = []
    for i in range(n):
        string.append(c)
    return "".join(string)


def histogram(array):
    for num in array:
        print(generate_n_chars(num, "*"))


def max_in_list(array):
    highest = 0
    for i in array:
        for j in array:
            if highest < j:
                highest = j
    return highest