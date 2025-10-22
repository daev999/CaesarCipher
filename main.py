from art import logo
print(logo)

# Caesar Cipher: Complete game with logo, restart, and non-letter handling
from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(caesar_dir, caesar_text, caesar_shift):
    if caesar_dir not in ["encode", "decode"]:
        print("Invalid direction! Use 'encode' or 'decode'.")
        return
    result_text = ""
    local_shift = caesar_shift  # Set shift for encoding/decoding
    if caesar_dir == "decode":
        local_shift *= -1  # Negate for decoding
    for char in caesar_text:
        if char not in alphabet:
            result_text += char
        else:
            position = alphabet.index(char)  # Find position
            new_position = (position + local_shift) % len(alphabet)  # Shift letter
            result_text += alphabet[new_position]  # Append letter
    print(f"Here is the {caesar_dir}d result: {result_text}")  # Print result

keep_running = True
while keep_running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(caesar_dir=direction, caesar_text=text, caesar_shift=shift)
    restart = input("Type 'yes' to continue, 'no' to exit:\n").lower()
    if restart == "no":
        print("Goodbye!")
        keep_running = False