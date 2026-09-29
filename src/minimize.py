def minimize(text):
    text = text.lower()
    return text

print(minimize('HELLO'))
print(minimize('HeLlO'))
print(minimize('123'))
print(minimize(''))
print(minimize('HELLO WORLD'))