# Character Count

message = input('Enter some words: ')
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character]+1

print(count)
