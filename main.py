from constants import *

class Enigma:
    def __init__(self, rotor1, rotor2, rotor3, reflector, plugboard):
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3
        self.reflector = reflector
        self.plugboard = plugboard

    def messaging(self, message=""):
        message = input("Enter message: ").upper() 
        print(message)
        return message
    
    def encrypt(self, message=""):
        message = self.messaging() # alot of repeated steps with minor changes, might take it out in to a method that is called for each rotor
        encrypted_rotor1 = []
        for i in message:
            if i.isalpha():
                i = i.upper()
                alpha_index = alphabet.index(i)
                scram1_in = rotor1[alpha_index]
                encrypted_rotor1.append(scram1_in)
            else:
                encrypted_rotor1.append(i)
        encrypted_rotor2 = []
        for j in encrypted_rotor1:
            if j.isalpha():
                scram1_index = alphabet.index(j)
                scram1_out = self.rotor2[scram1_index]
                encrypted_rotor2.append(scram1_out)
            else:
                encrypted_rotor2.append(j)
        encrypted_rotor3 = []
        for k in encrypted_rotor2:
            if k.isalpha():
                scram2_index = alphabet.index(k)
                scram2_out = self.rotor3[scram2_index]
                encrypted_rotor3.append(scram2_out)
            else:
                encrypted_rotor3.append(k)
        print("".join(encrypted_rotor1))
        print("".join(encrypted_rotor2))
        print("".join(encrypted_rotor3))

    def turn_rotor():
        pass

    def decrypt():
        pass

if __name__ == "__main__":
    enigma = Enigma(rotor1, rotor2, rotor3, reflector, plugboard)
    message = enigma.encrypt()