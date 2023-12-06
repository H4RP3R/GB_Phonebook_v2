from ui import *


if __name__ == '__main__':
    try:
        interface()
    except (KeyboardInterrupt, EOFError):
        print('\nПока!')
