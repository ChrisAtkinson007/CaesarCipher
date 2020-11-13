# Caesar cipher
text = input("Enter your message: ")
shift = int(input("Enter your shift: "))
cipher = ''
for char in text:
    if not char.isalpha():
        cipher+=char
        continue
    if((ord(char)+shift)>122):
        cipher+=chr(65+((ord(char)+shift)-1-122))
        print(65+(122-(ord(char)+shift)-1))
    else:
        cipher+=chr(ord(char)+shift)

print(cipher)
