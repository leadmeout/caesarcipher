alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):

    new_word = []

    for letter in text:

        try:
            new_index = alphabet.index(letter) + shift
            new_word.append(alphabet[new_index])
        except IndexError:
            new_index = new_index - len(alphabet)
            new_word.append(alphabet[new_index])
        except ValueError:
            if letter == ' ':
                new_word.append(' ')

    
    print(f'The encoded text is: {"".join(new_word)}')
        

def decrypt(text, shift):

    new_word = []

    for letter in text:

        try:
            new_index = alphabet.index(letter) - shift
            new_word.append(alphabet[new_index])
        except IndexError:
            new_index = new_index + len(alphabet)
            new_word.append(alphabet[new_index])
        except ValueError:
            if letter == ' ':
                new_word.append(' ')

    
    print(f'The encoded text is: {"".join(new_word)}')

def run_cipher():

    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)


run_cipher()

