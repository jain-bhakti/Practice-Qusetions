vowels = "aeiou"
def Iterative(s):
    count = 0
    for char in s:
        if char.lower() not in vowels and char.isalpha():
            count += 1
    return count

def Recursive(input_str):
    if input_str == '':
        return 0

    if input_str[0].lower() not in vowels and input_str[0].isalpha():
        return 1 + Recursive(input_str[1:])
    else:
        return Recursive(input_str[1:])

s = "Welcome to Educative!"
print(Iterative(s))
print(Recursive(s))
