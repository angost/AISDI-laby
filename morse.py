import argparse
import sys 


code = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..'
}

def main(arguments):
    filename = arguments[0]


    translation = ''
    with open(filename, 'r') as filehandle:
        data = filehandle.read()
    for char in data:
        if 65 <= ord(char.upper()) <= 90:
            translation += code[char.upper()]
            translation += ' '
        elif (char == ' ') and (translation[-2] != '/'):
            translation += '/ '
        elif char == '\n':
            translation += '\n'
    print(translation)
    return translation
    

if __name__ == "__main__":
    main(sys.argv[1:])
