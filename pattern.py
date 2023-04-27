def find_naive(pattern, text):
    index = []
    for i in range(len(text)):
        for j in range(len(pattern)):
            if text[i] == pattern[j]:
                # Znaleziono pelny wzorzec
                if j == len(pattern)-1:
                    index.append(i - len(pattern) + 1)
                i += 1
                if i == len(text):
                    break
            else:
                break
    return index



def find_KMP(pattern, text):
    index = []
    counter = 0
    for i in range(len(text)):
        if pattern[counter] == text[i]:
            counter += 1
        else:
            counter = 0
            if pattern[counter] == text[i]:
                counter = 1
        if counter == len(pattern):
            index.append(i - counter + 1)
            counter = 0
            if pattern[counter] == text[i]:
                counter = 1
    return index


def hash(string):
    hash_value = 0
    for i in range(len(string)):
        hash_value = ord(string[i]) * (10**i)
    return hash_value

def find_KR(pattern, text):
    index = []
    p_hash = hash(pattern)
    for i in range(len(text)):
        if i == 16:
            a=2
            pass
        if i + len(pattern) > len(text):
            break
        window = text[i:i+len(pattern)]
        if hash(window) == p_hash:
            patternFound = True
            for j, k in zip(window, pattern):
                if j != k:
                    patternFound = False
            if patternFound:
                index.append(i)
    return index



txt = 'AAL MA MAMALEGOMALEGO MALEGO KOTA'
pat = 'MALEGO'
# txt = "AAAAAAAAAAAAAAAAAA"
# pat = "A"
txt = 'MMAMMANN GBRGW'
pat = 'MANN'
print(find_naive(pat, txt))
# print(find_KMP(pat, txt))
print(find_KR(pat, txt))