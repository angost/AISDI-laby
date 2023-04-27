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
    # znak textu i znak patternu:
    #ROWNE
        # pierwsze rowne -> idziemy dalej
        # rowne w srodku patternu -> idziemy dalej
        # ostatnie rowne -> zapisz i PRZEGLADAJ W POPRZEDNICH
    #ROZNE
        # kolejne rozne -> idziemy dalej
        # pierwsze rozne (przerwanie patternu) -> PRZEGLADAJ W POPRZEDNICH

    index = []
    counter = 0
    if pattern == "":
        return index

    i = 0 # text start index
    while i < len(text):
        j = 0 # current pattern index
        while j < len(pattern):
            last_equal = (text[i+j] == pattern[j]) and (j == len(pattern)-1)
            first_different = (text[i+j] != pattern[j]) and (j == 0)

            if last_equal or first_different:
                if last_equal:
                    index.append(i)
                # szukanie w dotychczasowym fragmencie początku kolejnego patternu
                found_next_pattern_start = False
                for char in range(i+1, i+j+1):
                    if char == pattern[0]:
                        i = char
                        found_next_pattern_start = True
                        break
                if not found_next_pattern_start:
                    i += j

            j += 1
        i += 1
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
# pat = 'MALEGO'
# # txt = "AAAAAAAAAAAAAAAAAA"
# # # pat = "A"
# # txt = 'MMAMMANN GBRGW'
# # pat = 'MANN'
# txt = 'AAAA'
# pat = 'AAA'
# print(find_naive(pat, txt))
# print(find_KMP(pat, txt))
# print(find_KR(pat, txt))