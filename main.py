import datetime
from constants import *
from reflect import Reflector
from plug import Plugboard
from rot import Rotor
from enigma import EnigmaMachine

if __name__ == "__main__":
    plugboard = Plugboard({'A': 'B', 'C': 'D'})
    rotor1 = Rotor(rot1, "Q")
    rotor2 = Rotor(rot2, "E")
    rotor3 = Rotor(rot3, "V")
    reflector = Reflector(ref)
    enigma = EnigmaMachine([rotor1, rotor2, rotor3], reflector, plugboard)
    while True:
        command = input("Enter command (set r1/r2/r3 pos | set plug a:z | null | save | res | m | dec | show | exit): ").strip().lower()
        print("------------------------------------------------------------------------------------------")
        if command.startswith("set r"):
            _, rotor_id, position = command.split()
            position = int(position)
            if rotor_id == "r1":
                rotor1.set_position(position)
            elif rotor_id == "r2":
                rotor2.set_position(position)
            elif rotor_id == "r3":
                rotor3.set_position(position)
            print(f"Set {rotor_id} to position {position}.")

        elif command.startswith("set plug"):
            _, plug_config = command.split(maxsplit=1)
            a, z = plug_config.split(":")
            plugboard.add_connection(a, z)
            print(f"set plugboard connection {a.upper()} <-> {z.upper()}.")

        elif command == "null":
            enigma.reset()
            print("reset enigma machine to no plugboard settings and rotors at position 0")

        elif command == "save":
            enigma.save_state()
            print("saved current enigma machine settings")

        elif command == "res":
            enigma.load_state()
            print("loaded saved enigma machine settings")

        elif command == "show":
            print("current settings:")
            print(enigma.get_settings())

        elif command == "m":
            enigma.save_state()
            print("current settings:")
            print(enigma.get_settings())
            print("------------------------------------------------------------------------------------------")
            message = input("enter message to encrypt: ").strip()
            encrypted = enigma.process_message(message)
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("------------------------------------------------------------------------------------------")
            enigma.load_state() # resets back to the set settings after messeging so a new messege with same settings could be encrypted withoud manualy returning back to settings
            print(f"time: {current_time}")
            print(f"encrypted message: {encrypted}")
            print("------------------------------------------------------------------------------------------")

        elif command == "dec":
            enigma.load_state()
            print("current settings:")
            print(enigma.get_settings())
            message = input("enter message to decrypt: ").strip()
            decrypted = enigma.process_message(message)
            print(f"decrypted message: {decrypted}")

        elif command == "exit":
            print("exiting.")
            break

        else:
            print("invalid command. try again.")