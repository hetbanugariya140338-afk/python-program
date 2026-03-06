# Take input from user
s = input("Enter a string: ")

# a) Count number of vowels
vowels = "aeiouAEIOU"
vowel_count = 0
for ch in s:
    if ch in vowels:
        vowel_count += 1

print("Number of vowels:", vowel_count)

# b) Count length of string (without using len())
length = 0
for ch in s:
    length += 1

print("Length of string:", length)

# c) Reverse the string
reverse_str = ""
for ch in s:
    reverse_str = ch + reverse_str

print("Reversed string:", reverse_str)

# d) Find and replace operation
find_char = input("Enter character to find: ")
replace_char = input("Enter character to replace with: ")

new_str = ""
for ch in s:
    if ch == find_char:
        new_str += replace_char
    else:
        new_str += ch

print("String after replace:", new_str)

# e) Check palindrome
if s == reverse_str:
    print("The string is a palindrome")
else:
    print("The string is NOT a palindrome")
