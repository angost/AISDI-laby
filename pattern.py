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
    if pattern == "":
        return index
    i = 0 # text start index
    while i < len(text):
        j = 0 # current pattern index
        next_possible_pattern = None
        while (j < len(pattern)) and (i+j < len(text)):
            # Szukanie kolejnego poczatku patternu
            if (j > 0) and (not next_possible_pattern) and (text[i+j] == pattern[0]):
                next_possible_pattern = i+j

            # Znak textu i znak patternu:
            if text[i+j] == pattern[j]:
                # pierwsze rowne, rowne w srodku patternu -> idziemy dalej
                if j != len(pattern)-1:
                    j += 1
                # ostatnie rowne -> zapisz i PRZEJDZ DO KOLEJNEGO POCZATKU PATTERNU
                else:
                    index.append(i)
                    if next_possible_pattern:
                        i = next_possible_pattern
                    else:
                        i += len(pattern)
                    break
            else:
                # kolejne rozne -> idziemy dalej
                if j == 0:
                    i += 1
                # pierwsze rozne (przerwanie patternu) -> PRZEJDZ DO KOLEJNEGO POCZATKU PATTERNU
                else:
                    if next_possible_pattern:
                        i = next_possible_pattern
                    else:
                        i += j+1
                break
        if i+len(pattern) > len(text):
            break
    return index

def hash(string):
    hash_value = 0
    for i in range(len(string)):
        hash_value = ord(string[i]) * (10**i)
    return hash_value

def find_KR(pattern, text):
    index = []
    if pattern == "":
        return index
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



# txt = 'AAL MA MAMALEGOMALEGO MALEGO KOTA'
# # txt = 'ALA MA MALEGO KOTA'
# pat = 'MALEGO'
# txt = "AAAAAAAAAAAAAAAAAA"
# pat = "A"
# txt = "ABCDABCABCCABCXXXAAC"
# pat = "ABCC"

# text = "XXAXXAXABCAXABCABCCXABCCABCCXBCCXABCC"
# for i in range(len(text)):
#     print(i, text[i])

# txt = 'MMAMMANN GBRGW'
# pat = 'MANN'
# txt = 'AAAA'
# pat = 'AAA'
# print(find_naive(pat, txt))
# print(find_KMP(pat, txt))
# print(find_KR(pat, txt))