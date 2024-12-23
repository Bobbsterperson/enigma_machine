from constants import *
from plug import Plugboard
from enigma import EnigmaMachine
from rot import Rotor
from reflect import Reflector

def test_rotor_enigma_encryption():
    plugboard = Plugboard({'A': 'B', 'C': 'D'})
    rotor1 = Rotor(rot1, "Q")
    rotor2 = Rotor(rot2, "E")
    rotor3 = Rotor(rot3, "V")
    reflector = Reflector(ref)
    enigma = EnigmaMachine([rotor1, rotor2, rotor3], reflector, plugboard)
    encrypted = enigma.process_message("hello world")
    assert encrypted == "ZFEAM QKNGZ"

def test_rotor_movement():
    plugboard = Plugboard({'A': 'B', 'C': 'D'})
    rotor1 = Rotor(rot1, "Q")
    rotor2 = Rotor(rot2, "E")
    rotor3 = Rotor(rot3, "V")
    reflector = Reflector(ref)
    enigma = EnigmaMachine([rotor1, rotor2, rotor3], reflector, plugboard)
    encrypted = enigma.process_message("aaaaa")
    twocrypted = enigma.process_message("aaaaa")
    assert encrypted != "aaaaa"
    assert twocrypted != encrypted
    print(encrypted)
    print(twocrypted)

def test_rotor_decryption():
    plugboard = Plugboard({'A': 'B', 'C': 'D'})
    rotor1 = Rotor(rot1, "Q")
    rotor2 = Rotor(rot2, "E")
    rotor3 = Rotor(rot3, "V")
    reflector = Reflector(ref)
    enigma = EnigmaMachine([rotor1, rotor2, rotor3], reflector, plugboard)
    decrypted = enigma.process_message("ZFEAM QKNGZ")
    assert decrypted == "HELLO WORLD"
    print(decrypted)

