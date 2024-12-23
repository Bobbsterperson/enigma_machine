from constants import *

plugboard_mappings = {
    'A': 'Z', 'Z': 'A',
    'B': 'Y', 'Y': 'B',
    'C': 'X', 'X': 'C',
}

class Enigma:
    def __init__(self, rotor1, rotor2, rotor3, reflector, plugboard):
        self.rotor1 = list(rotor1)
        self.rotor2 = list(rotor2)
        self.rotor3 = list(rotor3)
        self.reflector = list(reflector)
        self.plugboard = plugboard
        self.rotor_positions = [0, 0, 0]

    def messaging(self):
        message = input("enter message: ").upper()
        return message

    def rotate_rotor(self, rotor, steps):
        return rotor[steps:] + rotor[:steps]

    def step_rotors(self):
        self.rotor_positions[0] += 1
        self.rotor1 = self.rotate_rotor(self.rotor1, 1)
        if self.rotor_positions[0] == 26:
            self.rotor_positions[0] = 0
            self.rotor_positions[1] += 1
            self.rotor2 = self.rotate_rotor(self.rotor2, 1)
        if self.rotor_positions[1] == 26:
            self.rotor_positions[1] = 0
            self.rotor_positions[2] += 1
            self.rotor3 = self.rotate_rotor(self.rotor3, 1)

    def plugboard_swap(self, char):
        return self.plugboard.get(char, char)

    def encrypt(self):
        message = self.messaging()
        encrypted_message = []
        for char in message:
            if char.isalpha():
                char = self.plugboard_swap(char)
                print(f"char trough plugboard {char}")
                char = self.rotor1[alphabet.index(char)]
                print(f"char trough rotor1 {char}")
                char = self.rotor2[alphabet.index(char)]
                print(f"char trough rotor2 {char}")
                char = self.rotor3[alphabet.index(char)]
                print(f"char trough rotor3 {char}")
                char = self.reflector[alphabet.index(char)]
                print(f"char trough refector {char}")
                char = alphabet[self.rotor3.index(char)]
                print(f"char trough rev rotor3 {char}")
                char = alphabet[self.rotor2.index(char)]
                print(f"char trough rev rotor2 {char}")
                char = alphabet[self.rotor1.index(char)]
                print(f"char trough rev rotor1 {char}")
                char = self.plugboard_swap(char)
                print(f"char trough rev plugboard back {char}")
                self.step_rotors()
            encrypted_message.append(char)
        print("".join(encrypted_message))

if __name__ == "__main__":
    enigma = Enigma(rotor1, rotor2, rotor3, reflector, plugboard_mappings)
    enigma.encrypt()
