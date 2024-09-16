from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, shift_direction):
    end_text = ""
    shift_offset = shift_amount
    if shift_direction == "decode": 
        shift_offset = shift_amount * -1
    
    for char in start_text:
        if char not in alphabet: 
            end_text += char
            continue
        char_index = alphabet.index(char)
        shifted_index = char_index + shift_offset
        wrapped_shifted_index = shifted_index % len(alphabet)
        end_text += alphabet[wrapped_shifted_index]
    
    print(f"The {shift_direction}d text is {end_text}")

def caesar_cypher():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amount=shift, shift_direction=direction)

    restart = input("\nDo you want to restart the cypher program? Type 'yes' if you want to restart, otherwise type 'no'.\n")
    if restart == "yes": caesar_cypher()

print(logo)
caesar_cypher()