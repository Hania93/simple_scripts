alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

is_running = True

def code_text(original_text, shift_amount, encode_or_decode):
    new_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for character in original_text:
        if character not in alphabet:
            new_text += character
        else:
            char_index = alphabet.index(character)

            new_index = char_index + shift_amount
            new_index %= len(alphabet)

            new_text += alphabet[new_index]

    return new_text

while is_running:
    direction = input("Which direction would you like to go? "
                      "Type 'encode' to encrypt or 'decode' to decrypt\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number? \n"))

    if direction == "encode":
        print(f"Encoded text: {code_text(text, shift, 'encode')}\n")

    elif direction == "decode":
        print(f"Decoded text: {code_text(text, shift, 'decode')}\n")
    else:
        print("Wrong value of direction. "
              "Please enter 'encode' or 'decode'")

    want_again = ''

    while want_again != "no" and want_again != "yes":
        want_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
        if want_again == "no":
            print("Goodbye!")
            is_running = False