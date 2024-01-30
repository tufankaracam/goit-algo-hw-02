from collections import deque


def isPalindrom(text):
    letters = deque()
    text = text.lower().replace(' ', '')
    count = len(text)
    count -= count % 2
    count = int(count / 2)

    for t in text:
        letters.append(t)

    for x in range(count):
        left = letters.popleft()
        right = letters.pop()
        if left != right:
            return False
    return True


print(isPalindrom('abb a'))
print(isPalindrom('lev el'))
print(isPalindrom('leve llev el'))
print(isPalindrom('xyyyxx'))
