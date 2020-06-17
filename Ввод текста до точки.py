def text_input():
    text = []
    while True:
        s = input()
        if s == '.':
            break
        else:
            text.append(s)
    return text

print(text_input())