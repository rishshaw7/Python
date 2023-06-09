c = 0

def vow(a):
    global c  # Declare c as a global variable
    if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u' or a == 'A' or a == 'E' or a == 'I' or a == 'O' or a == 'U':
        c = c + 1
    else:
        print("Vowel not found in the given string.")
     return c

vow("Hello")

