from pathlib import Path

file = Path('text_files/pi_million_digits.txt')
lines = file.read_text().splitlines()

pi_string = ''
for line in lines:
    pi_string += line.lstrip()

birthday = input("enter your bithda, in the mmddyy: ")

if birthday in pi_string:
    print(f"birthday contains into pi")
else:
    print(f"birthday no contains into pi")

print(pi_string[:52])
print(len(pi_string))