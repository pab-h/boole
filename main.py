from boole.Interpreter import Interpreter

def main() -> None:
    interpreter = Interpreter()    

    while True:
        try: 
            text = input(">>>")
            print(interpreter.eval(text))

        except EOFError:
            print("\n\nBye bye!\n")
            break

if __name__ == "__main__":
    main()
