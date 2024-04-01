from boole.Interpreter import Interpreter

import os.path as path

def main() -> None:
    interpreter = Interpreter()    

    i = 0

    print("Boole IDLE\n")
    while True:
        try: 
            text = input(f"In[{ i }] > ")

            if text == "_":
                print(interpreter.variables)
                continue

            if "file=" in text:
                filename  = text.split("file=").pop()
                text = ""

                if not path.exists(filename):
                    print(f"File {filename} not found")
                    continue

                with open(filename) as file:
                    text = file.read()
                    print(text)

            if text == "exit":
                raise EOFError()
            
            evalded = interpreter.eval(text)

            print(f"Out[{ i }] > { evalded }\n")
            i += 1

        except EOFError:
            print("\nBye, bye!\n")
            break

if __name__ == "__main__":
    main()
