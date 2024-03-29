from boole.Interpreter import Interpreter

def main() -> None:
    interpreter = Interpreter()    

    i = 0

    print("Boole IDLE\n")
    while True:
        try: 
            text = input(f"In[{ i }] > ")

            if "exit" in text:
                raise EOFError()
            
            evalded = interpreter.eval(text)

            print(f"Out[{ i }] > { evalded }\n")
            i += 1

        except EOFError:
            print("\nBye, bye!\n")
            break

if __name__ == "__main__":
    main()
